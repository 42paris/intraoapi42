from __future__ import annotations

import math
import time
from dataclasses import dataclass, replace
from threading import Lock
from typing import Callable, TypeVar, Union

import httpx
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

from .client import AuthenticatedClient
from .types import Response
from .models import Error

T = TypeVar("T")

class PagesError(Exception):
    def __init__(self, response):
        self.response = response
        super().__init__(f"Unexpected response while paging: {response.status_code} {response.parsed!r}")


def pages(
    sync_detailed_fn: Callable[..., Response[Union[Error, list[T]]]],
    *,
    client,
    page: int = 1,
    per_page: int = 100,
    show_progress: bool = True,
    **kwargs,
) -> list[T]:
    response = sync_detailed_fn(client=client, page=page, per_page=per_page, **kwargs)
    parsed = response.parsed

    if not isinstance(parsed, list):
        raise PagesError(response)

    total: list[T] = list(parsed)

    if "X-Total" not in response.headers:
        return total

    x_total = int(response.headers["X-Total"])
    resolved_per_page = int(response.headers.get("X-Per-Page", per_page))
    last_page = math.ceil(x_total / resolved_per_page)

    with tqdm(total=x_total, unit="item", initial=len(total), disable=not show_progress) as pbar:
        for next_page in range(page, last_page):
            response = sync_detailed_fn(client=client, page=next_page + 1, per_page=per_page, **kwargs)
            parsed = response.parsed
            if not isinstance(parsed, list):
                raise PagesError(response)
            total.extend(parsed)
            pbar.update(len(parsed))

    return total

def pages_threaded(
    sync_detailed_fn: Callable[..., Response[Union[Error, list[T]]]],
    *,
    client,
    page: int = 1,
    per_page: int = 100,
    max_workers: int = 8,
    show_progress: bool = True,
    **kwargs,
) -> list[T]:
    response = sync_detailed_fn(client=client, page=page, per_page=per_page, **kwargs)
    parsed = response.parsed

    if not isinstance(parsed, list):
        raise PagesError(response)

    results: dict[int, list[T]] = {page: list(parsed)}

    if "X-Total" not in response.headers:
        return results[page]

    x_total = int(response.headers["X-Total"])
    resolved_per_page = int(response.headers.get("X-Per-Page", per_page))
    last_page = math.ceil(x_total / resolved_per_page)

    remaining_pages = range(page + 1, last_page + 1)

    def fetch(pg: int) -> tuple[int, list[T]]:
        resp = sync_detailed_fn(client=client, page=pg, per_page=per_page, **kwargs)
        body = resp.parsed
        if not isinstance(body, list):
            raise PagesError(resp)
        return pg, body

    with tqdm(total=x_total, unit="item", initial=len(results[page]), disable=not show_progress) as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(fetch, pg): pg for pg in remaining_pages}

            for future in as_completed(futures):
                pg, body = future.result()
                results[pg] = body
                pbar.update(len(body))

    total: list[T] = []
    for pg in sorted(results):
        total.extend(results[pg])

    return total

@dataclass(frozen=True)
class Config:
    token_url: str
    server_url: str
    client_id: str = ""
    client_secret: str = ""
    scopes: tuple[str, ...] = ()

    def with_client_credentials(
        self,
        client_id: str,
        client_secret: str,
    ) -> Config:
        return replace(
            self,
            client_id=client_id,
            client_secret=client_secret,
        )

    def with_scopes(self, *scopes: str) -> Config:
        return replace(self, scopes=tuple(scopes))


ProductionConfig = Config(
    token_url="https://api.intra.42.fr/oauth/token",
    server_url="https://api.intra.42.fr/v2",
)

StagingConfig = Config(
    token_url="https://api.intra-staging.42.fr/oauth/token",
    server_url="https://api.intra-staging.42.fr/v2",
)


class RefreshableTokenSource:
    def __init__(
        self,
        config: Config,
        *,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._config = config
        self._clock = clock
        self._lock = Lock()
        self._access_token: str | None = None
        self._expires_at = 0.0

    def token(self) -> str:
        with self._lock:
            # Refresh one minute before the actual expiration time.
            if self._access_token is not None and self._clock() < self._expires_at - 60:
                return self._access_token

            response = httpx.post(
                self._config.token_url,
                data={
                    "grant_type": "client_credentials",
                    **({"scope": " ".join(self._config.scopes)} if self._config.scopes else {}),
                },
                auth=(
                    self._config.client_id,
                    self._config.client_secret,
                ),
                timeout=30.0,
            )
            response.raise_for_status()

            payload = response.json()
            access_token = payload["access_token"]
            expires_in = float(payload.get("expires_in", 3600))

            self._access_token = access_token
            self._expires_at = self._clock() + expires_in

            return access_token

    def invalidate(self) -> None:
        with self._lock:
            self._access_token = None
            self._expires_at = 0.0


class OAuth2ClientCredentials(httpx.Auth):
    requires_response_body = False

    def __init__(self, token_source: RefreshableTokenSource) -> None:
        self._token_source = token_source

    def sync_auth_flow(self, request: httpx.Request):
        for attempt in range(2):
            token = self._token_source.token()
            request.headers["Authorization"] = f"Bearer {token}"

            response = yield request

            if response.status_code != httpx.codes.UNAUTHORIZED:
                return

            if attempt == 1:
                return

            response.close()
            self._token_source.invalidate()


class RetryTransport(httpx.BaseTransport):
    rate_limit_retry_delay = 1.0
    rate_limit_max_retries = 3

    server_error_retry_delay = 0.5
    server_error_max_retries = 5

    network_error_retry_delay = 1.0
    network_error_max_retries = 5

    def __init__(
        self,
        transport: httpx.BaseTransport | None = None,
        *,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._transport = transport or httpx.HTTPTransport()
        self._sleep = sleep

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        body = request.content

        rate_limit_attempts = 0
        server_error_attempts = 0
        network_error_attempts = 0

        while True:
            retry_request = httpx.Request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                content=body,
                extensions=request.extensions,
            )

            try:
                response = self._transport.handle_request(retry_request)
            except (httpx.ReadTimeout, httpx.ConnectTimeout, httpx.ConnectError, httpx.RemoteProtocolError):
                if network_error_attempts >= self.network_error_max_retries:
                    raise
                network_error_attempts += 1
                self._sleep(self.network_error_retry_delay * network_error_attempts)
                continue

            if (
                response.status_code == httpx.codes.TOO_MANY_REQUESTS
                and rate_limit_attempts < self.rate_limit_max_retries
            ):
                rate_limit_attempts += 1
                response.read()
                response.close()
                self._sleep(self.rate_limit_retry_delay)
                continue

            if (
                response.status_code == httpx.codes.INTERNAL_SERVER_ERROR
                and server_error_attempts < self.server_error_max_retries
            ):
                server_error_attempts += 1
                response.read()
                response.close()
                self._sleep(self.server_error_retry_delay)
                continue

            return response

    def close(self) -> None:
        self._transport.close()


def NewClient(config: Config) -> AuthenticatedClient:
    token_source = RefreshableTokenSource(config)
    auth = OAuth2ClientCredentials(token_source)

    # Fetch an initial token because AuthenticatedClient requires one
    # in its constructor. The custom httpx.Auth handler remains
    # responsible for refreshing it after a 401 response.
    initial_token = token_source.token()

    http_client = httpx.Client(
        base_url=config.server_url,
        auth=auth,
        transport=RetryTransport(),
    )

    client = AuthenticatedClient(
        base_url=config.server_url,
        token=initial_token,
        prefix="Bearer",
    )

    client.set_httpx_client(http_client)

    return client

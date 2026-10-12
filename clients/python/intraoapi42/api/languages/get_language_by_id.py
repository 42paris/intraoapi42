from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_language_by_id_filter import GetLanguageByIdFilter
from ...models.get_language_by_id_range import GetLanguageByIdRange
from ...models.language import Language
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    sort: str | Unset = UNSET,
    filter_: GetLanguageByIdFilter | Unset = UNSET,
    range_: GetLanguageByIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sort"] = sort

    json_filter_: dict[str, Any] | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.to_dict()
    if not isinstance(json_filter_, Unset):
        params.update(json_filter_)

    json_range_: dict[str, Any] | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.to_dict()
    if not isinstance(json_range_, Unset):
        params.update(json_range_)

    params["page"] = page

    params["per_page"] = per_page

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/languages/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Language:
    if response.status_code == 200:
        response_200 = Language.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Language]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetLanguageByIdFilter | Unset = UNSET,
    range_: GetLanguageByIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | Language]:
    """Get a language by ID

    Args:
        id (int):
        sort (str | Unset):
        filter_ (GetLanguageByIdFilter | Unset):
        range_ (GetLanguageByIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Language]
    """

    kwargs = _get_kwargs(
        id=id,
        sort=sort,
        filter_=filter_,
        range_=range_,
        page=page,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetLanguageByIdFilter | Unset = UNSET,
    range_: GetLanguageByIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | Language | None:
    """Get a language by ID

    Args:
        id (int):
        sort (str | Unset):
        filter_ (GetLanguageByIdFilter | Unset):
        range_ (GetLanguageByIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Language
    """

    return sync_detailed(
        id=id,
        client=client,
        sort=sort,
        filter_=filter_,
        range_=range_,
        page=page,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetLanguageByIdFilter | Unset = UNSET,
    range_: GetLanguageByIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | Language]:
    """Get a language by ID

    Args:
        id (int):
        sort (str | Unset):
        filter_ (GetLanguageByIdFilter | Unset):
        range_ (GetLanguageByIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Language]
    """

    kwargs = _get_kwargs(
        id=id,
        sort=sort,
        filter_=filter_,
        range_=range_,
        page=page,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetLanguageByIdFilter | Unset = UNSET,
    range_: GetLanguageByIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | Language | None:
    """Get a language by ID

    Args:
        id (int):
        sort (str | Unset):
        filter_ (GetLanguageByIdFilter | Unset):
        range_ (GetLanguageByIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Language
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            sort=sort,
            filter_=filter_,
            range_=range_,
            page=page,
            per_page=per_page,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed

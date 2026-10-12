from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_users_by_cursus_filter import GetUsersByCursusFilter
from ...models.get_users_by_cursus_range import GetUsersByCursusRange
from ...models.light_user import LightUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cursus_id: str,
    *,
    sort: str | Unset = UNSET,
    filter_: GetUsersByCursusFilter | Unset = UNSET,
    range_: GetUsersByCursusRange | Unset = UNSET,
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

    params["per_page"] = per_page

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cursus/{cursus_id}/users".format(
            cursus_id=quote(str(cursus_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[LightUser]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LightUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | list[LightUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cursus_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetUsersByCursusFilter | Unset = UNSET,
    range_: GetUsersByCursusRange | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[LightUser]]:
    """Get a list of users by cursus

    Args:
        cursus_id (str):
        sort (str | Unset):
        filter_ (GetUsersByCursusFilter | Unset):
        range_ (GetUsersByCursusRange | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[LightUser]]
    """

    kwargs = _get_kwargs(
        cursus_id=cursus_id,
        sort=sort,
        filter_=filter_,
        range_=range_,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cursus_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetUsersByCursusFilter | Unset = UNSET,
    range_: GetUsersByCursusRange | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[LightUser] | None:
    """Get a list of users by cursus

    Args:
        cursus_id (str):
        sort (str | Unset):
        filter_ (GetUsersByCursusFilter | Unset):
        range_ (GetUsersByCursusRange | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[LightUser]
    """

    return sync_detailed(
        cursus_id=cursus_id,
        client=client,
        sort=sort,
        filter_=filter_,
        range_=range_,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    cursus_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetUsersByCursusFilter | Unset = UNSET,
    range_: GetUsersByCursusRange | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[LightUser]]:
    """Get a list of users by cursus

    Args:
        cursus_id (str):
        sort (str | Unset):
        filter_ (GetUsersByCursusFilter | Unset):
        range_ (GetUsersByCursusRange | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[LightUser]]
    """

    kwargs = _get_kwargs(
        cursus_id=cursus_id,
        sort=sort,
        filter_=filter_,
        range_=range_,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cursus_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetUsersByCursusFilter | Unset = UNSET,
    range_: GetUsersByCursusRange | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[LightUser] | None:
    """Get a list of users by cursus

    Args:
        cursus_id (str):
        sort (str | Unset):
        filter_ (GetUsersByCursusFilter | Unset):
        range_ (GetUsersByCursusRange | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[LightUser]
    """

    return (
        await asyncio_detailed(
            cursus_id=cursus_id,
            client=client,
            sort=sort,
            filter_=filter_,
            range_=range_,
            per_page=per_page,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed

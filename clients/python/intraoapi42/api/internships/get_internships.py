from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_internships_filter import GetInternshipsFilter
from ...models.get_internships_range import GetInternshipsRange
from ...models.internship import Internship
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort: str | Unset = UNSET,
    filter_: GetInternshipsFilter | Unset = UNSET,
    range_: GetInternshipsRange | Unset = UNSET,
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
        "url": "/internships",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[Internship]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Internship.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | list[Internship]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetInternshipsFilter | Unset = UNSET,
    range_: GetInternshipsRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[Internship]]:
    """🔑 Get a list of internships

    Args:
        sort (str | Unset):
        filter_ (GetInternshipsFilter | Unset):
        range_ (GetInternshipsRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Internship]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetInternshipsFilter | Unset = UNSET,
    range_: GetInternshipsRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[Internship] | None:
    """🔑 Get a list of internships

    Args:
        sort (str | Unset):
        filter_ (GetInternshipsFilter | Unset):
        range_ (GetInternshipsRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Internship]
    """

    return sync_detailed(
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
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetInternshipsFilter | Unset = UNSET,
    range_: GetInternshipsRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[Internship]]:
    """🔑 Get a list of internships

    Args:
        sort (str | Unset):
        filter_ (GetInternshipsFilter | Unset):
        range_ (GetInternshipsRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Internship]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetInternshipsFilter | Unset = UNSET,
    range_: GetInternshipsRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[Internship] | None:
    """🔑 Get a list of internships

    Args:
        sort (str | Unset):
        filter_ (GetInternshipsFilter | Unset):
        range_ (GetInternshipsRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Internship]
    """

    return (
        await asyncio_detailed(
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

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_projects_users_by_user_id_filter import GetProjectsUsersByUserIdFilter
from ...models.get_projects_users_by_user_id_range import GetProjectsUsersByUserIdRange
from ...models.project_user import ProjectUser
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    filter_: GetProjectsUsersByUserIdFilter | Unset = UNSET,
    range_: GetProjectsUsersByUserIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/users/{user_id}/projects_users".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[ProjectUser]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProjectUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | list[ProjectUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    filter_: GetProjectsUsersByUserIdFilter | Unset = UNSET,
    range_: GetProjectsUsersByUserIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[ProjectUser]]:
    """Get a list of projects users by a user Id

    Args:
        user_id (str):
        filter_ (GetProjectsUsersByUserIdFilter | Unset):
        range_ (GetProjectsUsersByUserIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[ProjectUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: str,
    *,
    client: AuthenticatedClient,
    filter_: GetProjectsUsersByUserIdFilter | Unset = UNSET,
    range_: GetProjectsUsersByUserIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[ProjectUser] | None:
    """Get a list of projects users by a user Id

    Args:
        user_id (str):
        filter_ (GetProjectsUsersByUserIdFilter | Unset):
        range_ (GetProjectsUsersByUserIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[ProjectUser]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        filter_=filter_,
        range_=range_,
        page=page,
        per_page=per_page,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    filter_: GetProjectsUsersByUserIdFilter | Unset = UNSET,
    range_: GetProjectsUsersByUserIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[ProjectUser]]:
    """Get a list of projects users by a user Id

    Args:
        user_id (str):
        filter_ (GetProjectsUsersByUserIdFilter | Unset):
        range_ (GetProjectsUsersByUserIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[ProjectUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: str,
    *,
    client: AuthenticatedClient,
    filter_: GetProjectsUsersByUserIdFilter | Unset = UNSET,
    range_: GetProjectsUsersByUserIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[ProjectUser] | None:
    """Get a list of projects users by a user Id

    Args:
        user_id (str):
        filter_ (GetProjectsUsersByUserIdFilter | Unset):
        range_ (GetProjectsUsersByUserIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[ProjectUser]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            filter_=filter_,
            range_=range_,
            page=page,
            per_page=per_page,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed

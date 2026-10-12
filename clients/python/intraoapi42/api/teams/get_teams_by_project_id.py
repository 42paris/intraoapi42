from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_teams_by_project_id_filter import GetTeamsByProjectIdFilter
from ...models.get_teams_by_project_id_range import GetTeamsByProjectIdRange
from ...models.light_team import LightTeam
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    sort: str | Unset = UNSET,
    filter_: GetTeamsByProjectIdFilter | Unset = UNSET,
    range_: GetTeamsByProjectIdRange | Unset = UNSET,
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
        "url": "/projects/{project_id}/teams".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[LightTeam]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LightTeam.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | list[LightTeam]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetTeamsByProjectIdFilter | Unset = UNSET,
    range_: GetTeamsByProjectIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[LightTeam]]:
    """Get a list of teams by a project Id

    Args:
        project_id (str):
        sort (str | Unset):
        filter_ (GetTeamsByProjectIdFilter | Unset):
        range_ (GetTeamsByProjectIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[LightTeam]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetTeamsByProjectIdFilter | Unset = UNSET,
    range_: GetTeamsByProjectIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[LightTeam] | None:
    """Get a list of teams by a project Id

    Args:
        project_id (str):
        sort (str | Unset):
        filter_ (GetTeamsByProjectIdFilter | Unset):
        range_ (GetTeamsByProjectIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[LightTeam]
    """

    return sync_detailed(
        project_id=project_id,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetTeamsByProjectIdFilter | Unset = UNSET,
    range_: GetTeamsByProjectIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[Error | list[LightTeam]]:
    """Get a list of teams by a project Id

    Args:
        project_id (str):
        sort (str | Unset):
        filter_ (GetTeamsByProjectIdFilter | Unset):
        range_ (GetTeamsByProjectIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[LightTeam]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    sort: str | Unset = UNSET,
    filter_: GetTeamsByProjectIdFilter | Unset = UNSET,
    range_: GetTeamsByProjectIdRange | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Error | list[LightTeam] | None:
    """Get a list of teams by a project Id

    Args:
        project_id (str):
        sort (str | Unset):
        filter_ (GetTeamsByProjectIdFilter | Unset):
        range_ (GetTeamsByProjectIdRange | Unset):
        page (int | Unset):
        per_page (int | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[LightTeam]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
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

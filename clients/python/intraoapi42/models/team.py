from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.light_team_user import LightTeamUser
    from ..models.scale_team import ScaleTeam


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        id (int):
        name (str):
        url (str):
        project_id (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (str):
        terminating_at (datetime.datetime | None):
        users (list[LightTeamUser]):
        locked (bool):
        validated (bool):
        closed (bool):
        repo_url (None | str):
        repo_uuid (str):
        locked_at (datetime.datetime | None):
        closed_at (datetime.datetime | None):
        project_session_id (int):
        project_gitlab_path (None | str):
        scale_teams (list[ScaleTeam]):
        final_mark (int | None | Unset):
    """

    id: int
    name: str
    url: str
    project_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: str
    terminating_at: datetime.datetime | None
    users: list[LightTeamUser]
    locked: bool
    validated: bool
    closed: bool
    repo_url: None | str
    repo_uuid: str
    locked_at: datetime.datetime | None
    closed_at: datetime.datetime | None
    project_session_id: int
    project_gitlab_path: None | str
    scale_teams: list[ScaleTeam]
    final_mark: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        project_id = self.project_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status = self.status

        terminating_at: None | str
        if isinstance(self.terminating_at, datetime.datetime):
            terminating_at = self.terminating_at.isoformat()
        else:
            terminating_at = self.terminating_at

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        locked = self.locked

        validated = self.validated

        closed = self.closed

        repo_url: None | str
        repo_url = self.repo_url

        repo_uuid = self.repo_uuid

        locked_at: None | str
        if isinstance(self.locked_at, datetime.datetime):
            locked_at = self.locked_at.isoformat()
        else:
            locked_at = self.locked_at

        closed_at: None | str
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        project_session_id = self.project_session_id

        project_gitlab_path: None | str
        project_gitlab_path = self.project_gitlab_path

        scale_teams = []
        for scale_teams_item_data in self.scale_teams:
            scale_teams_item = scale_teams_item_data.to_dict()
            scale_teams.append(scale_teams_item)

        final_mark: int | None | Unset
        if isinstance(self.final_mark, Unset):
            final_mark = UNSET
        else:
            final_mark = self.final_mark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "project_id": project_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "status": status,
                "terminating_at": terminating_at,
                "users": users,
                "locked?": locked,
                "validated?": validated,
                "closed?": closed,
                "repo_url": repo_url,
                "repo_uuid": repo_uuid,
                "locked_at": locked_at,
                "closed_at": closed_at,
                "project_session_id": project_session_id,
                "project_gitlab_path": project_gitlab_path,
                "scale_teams": scale_teams,
            }
        )
        if final_mark is not UNSET:
            field_dict["final_mark"] = final_mark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_team_user import LightTeamUser
        from ..models.scale_team import ScaleTeam

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url")

        project_id = d.pop("project_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status = d.pop("status")

        def _parse_terminating_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                terminating_at_type_0 = datetime.datetime.fromisoformat(data)

                return terminating_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        terminating_at = _parse_terminating_at(d.pop("terminating_at"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = LightTeamUser.from_dict(users_item_data)

            users.append(users_item)

        locked = d.pop("locked?")

        validated = d.pop("validated?")

        closed = d.pop("closed?")

        def _parse_repo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repo_url = _parse_repo_url(d.pop("repo_url"))

        repo_uuid = d.pop("repo_uuid")

        def _parse_locked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_at_type_0 = datetime.datetime.fromisoformat(data)

                return locked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        locked_at = _parse_locked_at(d.pop("locked_at"))

        def _parse_closed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        project_session_id = d.pop("project_session_id")

        def _parse_project_gitlab_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        project_gitlab_path = _parse_project_gitlab_path(d.pop("project_gitlab_path"))

        scale_teams = []
        _scale_teams = d.pop("scale_teams")
        for scale_teams_item_data in _scale_teams:
            scale_teams_item = ScaleTeam.from_dict(scale_teams_item_data)

            scale_teams.append(scale_teams_item)

        def _parse_final_mark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        final_mark = _parse_final_mark(d.pop("final_mark", UNSET))

        team = cls(
            id=id,
            name=name,
            url=url,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            terminating_at=terminating_at,
            users=users,
            locked=locked,
            validated=validated,
            closed=closed,
            repo_url=repo_url,
            repo_uuid=repo_uuid,
            locked_at=locked_at,
            closed_at=closed_at,
            project_session_id=project_session_id,
            project_gitlab_path=project_gitlab_path,
            scale_teams=scale_teams,
            final_mark=final_mark,
        )

        team.additional_properties = d
        return team

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

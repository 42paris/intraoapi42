from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_update_teams_users_attributes_type_0_item import TeamUpdateTeamsUsersAttributesType0Item


T = TypeVar("T", bound="TeamUpdate")


@_attrs_define
class TeamUpdate:
    """
    Attributes:
        project_id (int | None | Unset): The project id.
        name (None | str | Unset): The name.
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        locked_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
        final_mark (int | None | Unset): The final mark.
        repo_url (None | str | Unset): The repo url.
        repo_uuid (None | str | Unset): The repo uuid.
        deadline_at (int | None | Unset): The deadline at. Must be after today.
        terminating_at (datetime.datetime | None | Unset):
        project_session_id (int | None | Unset): The project session id.
        teams_users_attributes (list[TeamUpdateTeamsUsersAttributesType0Item] | None | Unset): The teams users
            attributes.
    """

    project_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    locked_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    final_mark: int | None | Unset = UNSET
    repo_url: None | str | Unset = UNSET
    repo_uuid: None | str | Unset = UNSET
    deadline_at: int | None | Unset = UNSET
    terminating_at: datetime.datetime | None | Unset = UNSET
    project_session_id: int | None | Unset = UNSET
    teams_users_attributes: list[TeamUpdateTeamsUsersAttributesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        locked_at: None | str | Unset
        if isinstance(self.locked_at, Unset):
            locked_at = UNSET
        elif isinstance(self.locked_at, datetime.datetime):
            locked_at = self.locked_at.isoformat()
        else:
            locked_at = self.locked_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        final_mark: int | None | Unset
        if isinstance(self.final_mark, Unset):
            final_mark = UNSET
        else:
            final_mark = self.final_mark

        repo_url: None | str | Unset
        if isinstance(self.repo_url, Unset):
            repo_url = UNSET
        else:
            repo_url = self.repo_url

        repo_uuid: None | str | Unset
        if isinstance(self.repo_uuid, Unset):
            repo_uuid = UNSET
        else:
            repo_uuid = self.repo_uuid

        deadline_at: int | None | Unset
        if isinstance(self.deadline_at, Unset):
            deadline_at = UNSET
        else:
            deadline_at = self.deadline_at

        terminating_at: None | str | Unset
        if isinstance(self.terminating_at, Unset):
            terminating_at = UNSET
        elif isinstance(self.terminating_at, datetime.datetime):
            terminating_at = self.terminating_at.isoformat()
        else:
            terminating_at = self.terminating_at

        project_session_id: int | None | Unset
        if isinstance(self.project_session_id, Unset):
            project_session_id = UNSET
        else:
            project_session_id = self.project_session_id

        teams_users_attributes: list[dict[str, Any]] | None | Unset
        if isinstance(self.teams_users_attributes, Unset):
            teams_users_attributes = UNSET
        elif isinstance(self.teams_users_attributes, list):
            teams_users_attributes = []
            for teams_users_attributes_type_0_item_data in self.teams_users_attributes:
                teams_users_attributes_type_0_item = teams_users_attributes_type_0_item_data.to_dict()
                teams_users_attributes.append(teams_users_attributes_type_0_item)

        else:
            teams_users_attributes = self.teams_users_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if locked_at is not UNSET:
            field_dict["locked_at"] = locked_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if final_mark is not UNSET:
            field_dict["final_mark"] = final_mark
        if repo_url is not UNSET:
            field_dict["repo_url"] = repo_url
        if repo_uuid is not UNSET:
            field_dict["repo_uuid"] = repo_uuid
        if deadline_at is not UNSET:
            field_dict["deadline_at"] = deadline_at
        if terminating_at is not UNSET:
            field_dict["terminating_at"] = terminating_at
        if project_session_id is not UNSET:
            field_dict["project_session_id"] = project_session_id
        if teams_users_attributes is not UNSET:
            field_dict["teams_users_attributes"] = teams_users_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_update_teams_users_attributes_type_0_item import TeamUpdateTeamsUsersAttributesType0Item

        d = dict(src_dict)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_locked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_at_type_0 = datetime.datetime.fromisoformat(data)

                return locked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        locked_at = _parse_locked_at(d.pop("locked_at", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_final_mark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        final_mark = _parse_final_mark(d.pop("final_mark", UNSET))

        def _parse_repo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo_url = _parse_repo_url(d.pop("repo_url", UNSET))

        def _parse_repo_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo_uuid = _parse_repo_uuid(d.pop("repo_uuid", UNSET))

        def _parse_deadline_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deadline_at = _parse_deadline_at(d.pop("deadline_at", UNSET))

        def _parse_terminating_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                terminating_at_type_0 = datetime.datetime.fromisoformat(data)

                return terminating_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        terminating_at = _parse_terminating_at(d.pop("terminating_at", UNSET))

        def _parse_project_session_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_session_id = _parse_project_session_id(d.pop("project_session_id", UNSET))

        def _parse_teams_users_attributes(data: object) -> list[TeamUpdateTeamsUsersAttributesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                teams_users_attributes_type_0 = []
                _teams_users_attributes_type_0 = data
                for teams_users_attributes_type_0_item_data in _teams_users_attributes_type_0:
                    teams_users_attributes_type_0_item = TeamUpdateTeamsUsersAttributesType0Item.from_dict(
                        teams_users_attributes_type_0_item_data
                    )

                    teams_users_attributes_type_0.append(teams_users_attributes_type_0_item)

                return teams_users_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TeamUpdateTeamsUsersAttributesType0Item] | None | Unset, data)

        teams_users_attributes = _parse_teams_users_attributes(d.pop("teams_users_attributes", UNSET))

        team_update = cls(
            project_id=project_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            locked_at=locked_at,
            closed_at=closed_at,
            final_mark=final_mark,
            repo_url=repo_url,
            repo_uuid=repo_uuid,
            deadline_at=deadline_at,
            terminating_at=terminating_at,
            project_session_id=project_session_id,
            teams_users_attributes=teams_users_attributes,
        )

        team_update.additional_properties = d
        return team_update

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

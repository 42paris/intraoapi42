from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectUserUpdate")


@_attrs_define
class ProjectUserUpdate:
    """
    Attributes:
        id (int | None | Unset): The id.
        project_id (int | None | Unset): The project id.
        user_id (int | None | Unset): The user id. Must be unique in the scope of a given project.
        created_at (datetime.datetime | None | Unset): The created at.
        updated_at (datetime.datetime | None | Unset): The updated at.
        occurrence (int | None | Unset): The occurrence. Default to 0. Default: 0.
        final_mark (int | None | Unset): The final mark.
        retriable_at (datetime.datetime | None | Unset): The retriable at.
        marked_at (datetime.datetime | None | Unset): The marked at.
        status (None | str | Unset): The status. Default to unknown. Default: 'unknown'.
        skip_check_permission (None | str | Unset): The skip check permission.
    """

    id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    user_id: int | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    occurrence: int | None | Unset = 0
    final_mark: int | None | Unset = UNSET
    retriable_at: datetime.datetime | None | Unset = UNSET
    marked_at: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = "unknown"
    skip_check_permission: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

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

        occurrence: int | None | Unset
        if isinstance(self.occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = self.occurrence

        final_mark: int | None | Unset
        if isinstance(self.final_mark, Unset):
            final_mark = UNSET
        else:
            final_mark = self.final_mark

        retriable_at: None | str | Unset
        if isinstance(self.retriable_at, Unset):
            retriable_at = UNSET
        elif isinstance(self.retriable_at, datetime.datetime):
            retriable_at = self.retriable_at.isoformat()
        else:
            retriable_at = self.retriable_at

        marked_at: None | str | Unset
        if isinstance(self.marked_at, Unset):
            marked_at = UNSET
        elif isinstance(self.marked_at, datetime.datetime):
            marked_at = self.marked_at.isoformat()
        else:
            marked_at = self.marked_at

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        skip_check_permission: None | str | Unset
        if isinstance(self.skip_check_permission, Unset):
            skip_check_permission = UNSET
        else:
            skip_check_permission = self.skip_check_permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if final_mark is not UNSET:
            field_dict["final_mark"] = final_mark
        if retriable_at is not UNSET:
            field_dict["retriable_at"] = retriable_at
        if marked_at is not UNSET:
            field_dict["marked_at"] = marked_at
        if status is not UNSET:
            field_dict["status"] = status
        if skip_check_permission is not UNSET:
            field_dict["skip_check_permission"] = skip_check_permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

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

        def _parse_occurrence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occurrence = _parse_occurrence(d.pop("occurrence", UNSET))

        def _parse_final_mark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        final_mark = _parse_final_mark(d.pop("final_mark", UNSET))

        def _parse_retriable_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retriable_at_type_0 = datetime.datetime.fromisoformat(data)

                return retriable_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retriable_at = _parse_retriable_at(d.pop("retriable_at", UNSET))

        def _parse_marked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marked_at_type_0 = datetime.datetime.fromisoformat(data)

                return marked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        marked_at = _parse_marked_at(d.pop("marked_at", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_skip_check_permission(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skip_check_permission = _parse_skip_check_permission(d.pop("skip_check_permission", UNSET))

        project_user_update = cls(
            id=id,
            project_id=project_id,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            occurrence=occurrence,
            final_mark=final_mark,
            retriable_at=retriable_at,
            marked_at=marked_at,
            status=status,
            skip_check_permission=skip_check_permission,
        )

        project_user_update.additional_properties = d
        return project_user_update

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

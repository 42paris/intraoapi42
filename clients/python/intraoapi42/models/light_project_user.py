from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.light_project import LightProject


T = TypeVar("T", bound="LightProjectUser")


@_attrs_define
class LightProjectUser:
    """
    Attributes:
        id (int):
        occurrence (int):
        final_mark (int | None):
        status (str):
        validated (bool | None):
        current_team_id (int):
        project (LightProject):
        cursus_ids (list[int]):
        marked_at (datetime.datetime | None):
        marked (bool | None):
        retriable_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    occurrence: int
    final_mark: int | None
    status: str
    validated: bool | None
    current_team_id: int
    project: LightProject
    cursus_ids: list[int]
    marked_at: datetime.datetime | None
    marked: bool | None
    retriable_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        occurrence = self.occurrence

        final_mark: int | None
        final_mark = self.final_mark

        status = self.status

        validated: bool | None
        validated = self.validated

        current_team_id = self.current_team_id

        project = self.project.to_dict()

        cursus_ids = self.cursus_ids

        marked_at: None | str
        if isinstance(self.marked_at, datetime.datetime):
            marked_at = self.marked_at.isoformat()
        else:
            marked_at = self.marked_at

        marked: bool | None
        marked = self.marked

        retriable_at: None | str
        if isinstance(self.retriable_at, datetime.datetime):
            retriable_at = self.retriable_at.isoformat()
        else:
            retriable_at = self.retriable_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "occurrence": occurrence,
                "final_mark": final_mark,
                "status": status,
                "validated?": validated,
                "current_team_id": current_team_id,
                "project": project,
                "cursus_ids": cursus_ids,
                "marked_at": marked_at,
                "marked": marked,
                "retriable_at": retriable_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_project import LightProject

        d = dict(src_dict)
        id = d.pop("id")

        occurrence = d.pop("occurrence")

        def _parse_final_mark(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        final_mark = _parse_final_mark(d.pop("final_mark"))

        status = d.pop("status")

        def _parse_validated(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        validated = _parse_validated(d.pop("validated?"))

        current_team_id = d.pop("current_team_id")

        project = LightProject.from_dict(d.pop("project"))

        cursus_ids = cast(list[int], d.pop("cursus_ids"))

        def _parse_marked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marked_at_type_0 = datetime.datetime.fromisoformat(data)

                return marked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        marked_at = _parse_marked_at(d.pop("marked_at"))

        def _parse_marked(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        marked = _parse_marked(d.pop("marked"))

        def _parse_retriable_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retriable_at_type_0 = datetime.datetime.fromisoformat(data)

                return retriable_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        retriable_at = _parse_retriable_at(d.pop("retriable_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        light_project_user = cls(
            id=id,
            occurrence=occurrence,
            final_mark=final_mark,
            status=status,
            validated=validated,
            current_team_id=current_team_id,
            project=project,
            cursus_ids=cursus_ids,
            marked_at=marked_at,
            marked=marked,
            retriable_at=retriable_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        light_project_user.additional_properties = d
        return light_project_user

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

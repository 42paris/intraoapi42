from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CampusUser")


@_attrs_define
class CampusUser:
    """
    Attributes:
        id (int):
        user_id (int):
        campus_id (int):
        is_primary (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    user_id: int
    campus_id: int
    is_primary: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        campus_id = self.campus_id

        is_primary = self.is_primary

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "campus_id": campus_id,
                "is_primary": is_primary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        campus_id = d.pop("campus_id")

        is_primary = d.pop("is_primary")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        campus_user = cls(
            id=id,
            user_id=user_id,
            campus_id=campus_id,
            is_primary=is_primary,
            created_at=created_at,
            updated_at=updated_at,
        )

        campus_user.additional_properties = d
        return campus_user

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

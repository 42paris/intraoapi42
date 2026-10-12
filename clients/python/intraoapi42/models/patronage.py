from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Patronage")


@_attrs_define
class Patronage:
    """
    Attributes:
        id (int):
        ongoing (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        user_id (int | Unset):
        godson_id (int | Unset):
        godfather_id (int | Unset):
    """

    id: int
    ongoing: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: int | Unset = UNSET
    godson_id: int | Unset = UNSET
    godfather_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ongoing = self.ongoing

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        godson_id = self.godson_id

        godfather_id = self.godfather_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ongoing": ongoing,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if godson_id is not UNSET:
            field_dict["godson_id"] = godson_id
        if godfather_id is not UNSET:
            field_dict["godfather_id"] = godfather_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ongoing = d.pop("ongoing")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        user_id = d.pop("user_id", UNSET)

        godson_id = d.pop("godson_id", UNSET)

        godfather_id = d.pop("godfather_id", UNSET)

        patronage = cls(
            id=id,
            ongoing=ongoing,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            godson_id=godson_id,
            godfather_id=godfather_id,
        )

        patronage.additional_properties = d
        return patronage

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

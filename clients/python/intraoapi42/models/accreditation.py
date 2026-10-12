from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Accreditation")


@_attrs_define
class Accreditation:
    """
    Attributes:
        id (int):
        name (str):
        user_id (int):
        cursus_id (int):
        validated (bool):
    """

    id: int
    name: str
    user_id: int
    cursus_id: int
    validated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        user_id = self.user_id

        cursus_id = self.cursus_id

        validated = self.validated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "user_id": user_id,
                "cursus_id": cursus_id,
                "validated": validated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        user_id = d.pop("user_id")

        cursus_id = d.pop("cursus_id")

        validated = d.pop("validated")

        accreditation = cls(
            id=id,
            name=name,
            user_id=user_id,
            cursus_id=cursus_id,
            validated=validated,
        )

        accreditation.additional_properties = d
        return accreditation

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

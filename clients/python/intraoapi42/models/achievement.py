from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Achievement")


@_attrs_define
class Achievement:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        tier (str):
        kind (str):
        visible (bool):
        image (str):
        users_url (str):
        nbr_of_success (int | None | Unset):
    """

    id: int
    name: str
    description: str
    tier: str
    kind: str
    visible: bool
    image: str
    users_url: str
    nbr_of_success: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        tier = self.tier

        kind = self.kind

        visible = self.visible

        image = self.image

        users_url = self.users_url

        nbr_of_success: int | None | Unset
        if isinstance(self.nbr_of_success, Unset):
            nbr_of_success = UNSET
        else:
            nbr_of_success = self.nbr_of_success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "tier": tier,
                "kind": kind,
                "visible": visible,
                "image": image,
                "users_url": users_url,
            }
        )
        if nbr_of_success is not UNSET:
            field_dict["nbr_of_success"] = nbr_of_success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        tier = d.pop("tier")

        kind = d.pop("kind")

        visible = d.pop("visible")

        image = d.pop("image")

        users_url = d.pop("users_url")

        def _parse_nbr_of_success(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nbr_of_success = _parse_nbr_of_success(d.pop("nbr_of_success", UNSET))

        achievement = cls(
            id=id,
            name=name,
            description=description,
            tier=tier,
            kind=kind,
            visible=visible,
            image=image,
            users_url=users_url,
            nbr_of_success=nbr_of_success,
        )

        achievement.additional_properties = d
        return achievement

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

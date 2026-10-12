from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserImageVersions")


@_attrs_define
class UserImageVersions:
    """
    Attributes:
        large (str): URL to the large version of the user's image.
        medium (str): URL to the medium version of the user's image.
        small (str): URL to the small version of the user's image.
        micro (str): URL to the micro version of the user's image.
    """

    large: str
    medium: str
    small: str
    micro: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        large = self.large

        medium = self.medium

        small = self.small

        micro = self.micro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "large": large,
                "medium": medium,
                "small": small,
                "micro": micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        large = d.pop("large")

        medium = d.pop("medium")

        small = d.pop("small")

        micro = d.pop("micro")

        user_image_versions = cls(
            large=large,
            medium=medium,
            small=small,
            micro=micro,
        )

        user_image_versions.additional_properties = d
        return user_image_versions

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

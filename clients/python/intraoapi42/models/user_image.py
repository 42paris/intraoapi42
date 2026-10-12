from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_image_versions import UserImageVersions


T = TypeVar("T", bound="UserImage")


@_attrs_define
class UserImage:
    """
    Attributes:
        link (str): The URL to the user's image.
        versions (UserImageVersions):
    """

    link: str
    versions: UserImageVersions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        versions = self.versions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_image_versions import UserImageVersions

        d = dict(src_dict)
        link = d.pop("link")

        versions = UserImageVersions.from_dict(d.pop("versions"))

        user_image = cls(
            link=link,
            versions=versions,
        )

        user_image.additional_properties = d
        return user_image

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

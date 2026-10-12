from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Coalition")


@_attrs_define
class Coalition:
    """
    Attributes:
        id (int):
        name (str):
        slug (str):
        color (str):
        score (int):
        user_id (int):
        image_url (None | str | Unset):
        cover_url (None | str | Unset):
    """

    id: int
    name: str
    slug: str
    color: str
    score: int
    user_id: int
    image_url: None | str | Unset = UNSET
    cover_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        color = self.color

        score = self.score

        user_id = self.user_id

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        cover_url: None | str | Unset
        if isinstance(self.cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = self.cover_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "color": color,
                "score": score,
                "user_id": user_id,
            }
        )
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        color = d.pop("color")

        score = d.pop("score")

        user_id = d.pop("user_id")

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        def _parse_cover_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_url = _parse_cover_url(d.pop("cover_url", UNSET))

        coalition = cls(
            id=id,
            name=name,
            slug=slug,
            color=color,
            score=score,
            user_id=user_id,
            image_url=image_url,
            cover_url=cover_url,
        )

        coalition.additional_properties = d
        return coalition

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

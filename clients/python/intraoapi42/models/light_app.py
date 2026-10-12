from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightApp")


@_attrs_define
class LightApp:
    """
    Attributes:
        id (int):
        name (str):
        public (bool):
        scopes (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        rate_limit (int):
        description (None | str | Unset):
        image (None | str | Unset):
        website (None | str | Unset):
    """

    id: int
    name: str
    public: bool
    scopes: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    rate_limit: int
    description: None | str | Unset = UNSET
    image: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        public = self.public

        scopes = self.scopes

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        rate_limit = self.rate_limit

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "public": public,
                "scopes": scopes,
                "created_at": created_at,
                "updated_at": updated_at,
                "rate_limit": rate_limit,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        public = d.pop("public")

        scopes = cast(list[str], d.pop("scopes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        rate_limit = d.pop("rate_limit")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        light_app = cls(
            id=id,
            name=name,
            public=public,
            scopes=scopes,
            created_at=created_at,
            updated_at=updated_at,
            rate_limit=rate_limit,
            description=description,
            image=image,
            website=website,
        )

        light_app.additional_properties = d
        return light_app

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

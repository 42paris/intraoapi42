from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LightCampus")


@_attrs_define
class LightCampus:
    """
    Attributes:
        id (int):
        name (str):
        time_zone (str):
        users_count (int):
        vogsphere_id (int):
        country (str):
        address (str):
        zip_ (str):
        city (str):
        website (str):
        facebook (str):
        twitter (str):
        active (bool):
        public (bool):
        email_extension (str):
        default_hidden_phone (bool):
    """

    id: int
    name: str
    time_zone: str
    users_count: int
    vogsphere_id: int
    country: str
    address: str
    zip_: str
    city: str
    website: str
    facebook: str
    twitter: str
    active: bool
    public: bool
    email_extension: str
    default_hidden_phone: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        time_zone = self.time_zone

        users_count = self.users_count

        vogsphere_id = self.vogsphere_id

        country = self.country

        address = self.address

        zip_ = self.zip_

        city = self.city

        website = self.website

        facebook = self.facebook

        twitter = self.twitter

        active = self.active

        public = self.public

        email_extension = self.email_extension

        default_hidden_phone = self.default_hidden_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "time_zone": time_zone,
                "users_count": users_count,
                "vogsphere_id": vogsphere_id,
                "country": country,
                "address": address,
                "zip": zip_,
                "city": city,
                "website": website,
                "facebook": facebook,
                "twitter": twitter,
                "active": active,
                "public": public,
                "email_extension": email_extension,
                "default_hidden_phone": default_hidden_phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        time_zone = d.pop("time_zone")

        users_count = d.pop("users_count")

        vogsphere_id = d.pop("vogsphere_id")

        country = d.pop("country")

        address = d.pop("address")

        zip_ = d.pop("zip")

        city = d.pop("city")

        website = d.pop("website")

        facebook = d.pop("facebook")

        twitter = d.pop("twitter")

        active = d.pop("active")

        public = d.pop("public")

        email_extension = d.pop("email_extension")

        default_hidden_phone = d.pop("default_hidden_phone")

        light_campus = cls(
            id=id,
            name=name,
            time_zone=time_zone,
            users_count=users_count,
            vogsphere_id=vogsphere_id,
            country=country,
            address=address,
            zip_=zip_,
            city=city,
            website=website,
            facebook=facebook,
            twitter=twitter,
            active=active,
            public=public,
            email_extension=email_extension,
            default_hidden_phone=default_hidden_phone,
        )

        light_campus.additional_properties = d
        return light_campus

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

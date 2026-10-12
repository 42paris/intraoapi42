from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language


T = TypeVar("T", bound="Campus")


@_attrs_define
class Campus:
    """
    Attributes:
        id (int):
        name (str):
        time_zone (str):
        users_count (int):
        vogsphere_id (int):
        country (str):
        city (str):
        active (bool):
        public (bool):
        email_extension (str):
        language (Language | Unset):
        address (str | Unset):
        zip_ (str | Unset):
        website (str | Unset):
        facebook (str | Unset):
        twitter (str | Unset):
        default_hidden_phone (bool | Unset):
    """

    id: int
    name: str
    time_zone: str
    users_count: int
    vogsphere_id: int
    country: str
    city: str
    active: bool
    public: bool
    email_extension: str
    language: Language | Unset = UNSET
    address: str | Unset = UNSET
    zip_: str | Unset = UNSET
    website: str | Unset = UNSET
    facebook: str | Unset = UNSET
    twitter: str | Unset = UNSET
    default_hidden_phone: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        time_zone = self.time_zone

        users_count = self.users_count

        vogsphere_id = self.vogsphere_id

        country = self.country

        city = self.city

        active = self.active

        public = self.public

        email_extension = self.email_extension

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        address = self.address

        zip_ = self.zip_

        website = self.website

        facebook = self.facebook

        twitter = self.twitter

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
                "city": city,
                "active": active,
                "public": public,
                "email_extension": email_extension,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if address is not UNSET:
            field_dict["address"] = address
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if website is not UNSET:
            field_dict["website"] = website
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if default_hidden_phone is not UNSET:
            field_dict["default_hidden_phone"] = default_hidden_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language import Language

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        time_zone = d.pop("time_zone")

        users_count = d.pop("users_count")

        vogsphere_id = d.pop("vogsphere_id")

        country = d.pop("country")

        city = d.pop("city")

        active = d.pop("active")

        public = d.pop("public")

        email_extension = d.pop("email_extension")

        _language = d.pop("language", UNSET)
        language: Language | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language.from_dict(_language)

        address = d.pop("address", UNSET)

        zip_ = d.pop("zip", UNSET)

        website = d.pop("website", UNSET)

        facebook = d.pop("facebook", UNSET)

        twitter = d.pop("twitter", UNSET)

        default_hidden_phone = d.pop("default_hidden_phone", UNSET)

        campus = cls(
            id=id,
            name=name,
            time_zone=time_zone,
            users_count=users_count,
            vogsphere_id=vogsphere_id,
            country=country,
            city=city,
            active=active,
            public=public,
            email_extension=email_extension,
            language=language,
            address=address,
            zip_=zip_,
            website=website,
            facebook=facebook,
            twitter=twitter,
            default_hidden_phone=default_hidden_phone,
        )

        campus.additional_properties = d
        return campus

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

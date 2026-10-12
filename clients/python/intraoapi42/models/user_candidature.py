from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_candidature_gender import UserCandidatureGender, check_user_candidature_gender
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCandidature")


@_attrs_define
class UserCandidature:
    """
    Attributes:
        id (int):
        user_id (int):
        birth_city (str):
        postal_street (str):
        postal_city (str):
        postal_zip_code (str):
        postal_country (str):
        contact_affiliation (str):
        contact_last_name (str):
        contact_first_name (str):
        contact_phone1 (str):
        language (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        phone (str):
        email (str):
        pin (str):
        phone_country_code (str):
        hidden_phone (bool):
        birth_date (datetime.date | Unset):
        gender (UserCandidatureGender | Unset):
        zip_code (None | str | Unset):
        country (None | str | Unset):
        birth_country (None | str | Unset):
        postal_complement (None | str | Unset):
        contact_phone2 (None | str | Unset):
        max_level_memory (float | None | Unset):
        max_level_logic (float | None | Unset):
        other_information (None | str | Unset):
        meeting_date (datetime.datetime | None | Unset):
        piscine_date (datetime.datetime | None | Unset):
    """

    id: int
    user_id: int
    birth_city: str
    postal_street: str
    postal_city: str
    postal_zip_code: str
    postal_country: str
    contact_affiliation: str
    contact_last_name: str
    contact_first_name: str
    contact_phone1: str
    language: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    phone: str
    email: str
    pin: str
    phone_country_code: str
    hidden_phone: bool
    birth_date: datetime.date | Unset = UNSET
    gender: UserCandidatureGender | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    birth_country: None | str | Unset = UNSET
    postal_complement: None | str | Unset = UNSET
    contact_phone2: None | str | Unset = UNSET
    max_level_memory: float | None | Unset = UNSET
    max_level_logic: float | None | Unset = UNSET
    other_information: None | str | Unset = UNSET
    meeting_date: datetime.datetime | None | Unset = UNSET
    piscine_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        birth_city = self.birth_city

        postal_street = self.postal_street

        postal_city = self.postal_city

        postal_zip_code = self.postal_zip_code

        postal_country = self.postal_country

        contact_affiliation = self.contact_affiliation

        contact_last_name = self.contact_last_name

        contact_first_name = self.contact_first_name

        contact_phone1 = self.contact_phone1

        language = self.language

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        phone = self.phone

        email = self.email

        pin = self.pin

        phone_country_code = self.phone_country_code

        hidden_phone = self.hidden_phone

        birth_date: str | Unset = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.isoformat()

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender

        zip_code: None | str | Unset
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        birth_country: None | str | Unset
        if isinstance(self.birth_country, Unset):
            birth_country = UNSET
        else:
            birth_country = self.birth_country

        postal_complement: None | str | Unset
        if isinstance(self.postal_complement, Unset):
            postal_complement = UNSET
        else:
            postal_complement = self.postal_complement

        contact_phone2: None | str | Unset
        if isinstance(self.contact_phone2, Unset):
            contact_phone2 = UNSET
        else:
            contact_phone2 = self.contact_phone2

        max_level_memory: float | None | Unset
        if isinstance(self.max_level_memory, Unset):
            max_level_memory = UNSET
        else:
            max_level_memory = self.max_level_memory

        max_level_logic: float | None | Unset
        if isinstance(self.max_level_logic, Unset):
            max_level_logic = UNSET
        else:
            max_level_logic = self.max_level_logic

        other_information: None | str | Unset
        if isinstance(self.other_information, Unset):
            other_information = UNSET
        else:
            other_information = self.other_information

        meeting_date: None | str | Unset
        if isinstance(self.meeting_date, Unset):
            meeting_date = UNSET
        elif isinstance(self.meeting_date, datetime.datetime):
            meeting_date = self.meeting_date.isoformat()
        else:
            meeting_date = self.meeting_date

        piscine_date: None | str | Unset
        if isinstance(self.piscine_date, Unset):
            piscine_date = UNSET
        elif isinstance(self.piscine_date, datetime.datetime):
            piscine_date = self.piscine_date.isoformat()
        else:
            piscine_date = self.piscine_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "birth_city": birth_city,
                "postal_street": postal_street,
                "postal_city": postal_city,
                "postal_zip_code": postal_zip_code,
                "postal_country": postal_country,
                "contact_affiliation": contact_affiliation,
                "contact_last_name": contact_last_name,
                "contact_first_name": contact_first_name,
                "contact_phone1": contact_phone1,
                "language": language,
                "created_at": created_at,
                "updated_at": updated_at,
                "phone": phone,
                "email": email,
                "pin": pin,
                "phone_country_code": phone_country_code,
                "hidden_phone": hidden_phone,
            }
        )
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if gender is not UNSET:
            field_dict["gender"] = gender
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if country is not UNSET:
            field_dict["country"] = country
        if birth_country is not UNSET:
            field_dict["birth_country"] = birth_country
        if postal_complement is not UNSET:
            field_dict["postal_complement"] = postal_complement
        if contact_phone2 is not UNSET:
            field_dict["contact_phone2"] = contact_phone2
        if max_level_memory is not UNSET:
            field_dict["max_level_memory"] = max_level_memory
        if max_level_logic is not UNSET:
            field_dict["max_level_logic"] = max_level_logic
        if other_information is not UNSET:
            field_dict["other_information"] = other_information
        if meeting_date is not UNSET:
            field_dict["meeting_date"] = meeting_date
        if piscine_date is not UNSET:
            field_dict["piscine_date"] = piscine_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        birth_city = d.pop("birth_city")

        postal_street = d.pop("postal_street")

        postal_city = d.pop("postal_city")

        postal_zip_code = d.pop("postal_zip_code")

        postal_country = d.pop("postal_country")

        contact_affiliation = d.pop("contact_affiliation")

        contact_last_name = d.pop("contact_last_name")

        contact_first_name = d.pop("contact_first_name")

        contact_phone1 = d.pop("contact_phone1")

        language = d.pop("language")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        phone = d.pop("phone")

        email = d.pop("email")

        pin = d.pop("pin")

        phone_country_code = d.pop("phone_country_code")

        hidden_phone = d.pop("hidden_phone")

        _birth_date = d.pop("birth_date", UNSET)
        birth_date: datetime.date | Unset
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = datetime.date.fromisoformat(_birth_date)

        _gender = d.pop("gender", UNSET)
        gender: UserCandidatureGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = check_user_candidature_gender(_gender)

        def _parse_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_code = _parse_zip_code(d.pop("zip_code", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_birth_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birth_country = _parse_birth_country(d.pop("birth_country", UNSET))

        def _parse_postal_complement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_complement = _parse_postal_complement(d.pop("postal_complement", UNSET))

        def _parse_contact_phone2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_phone2 = _parse_contact_phone2(d.pop("contact_phone2", UNSET))

        def _parse_max_level_memory(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_level_memory = _parse_max_level_memory(d.pop("max_level_memory", UNSET))

        def _parse_max_level_logic(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_level_logic = _parse_max_level_logic(d.pop("max_level_logic", UNSET))

        def _parse_other_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_information = _parse_other_information(d.pop("other_information", UNSET))

        def _parse_meeting_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meeting_date_type_0 = datetime.datetime.fromisoformat(data)

                return meeting_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        meeting_date = _parse_meeting_date(d.pop("meeting_date", UNSET))

        def _parse_piscine_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                piscine_date_type_0 = datetime.datetime.fromisoformat(data)

                return piscine_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        piscine_date = _parse_piscine_date(d.pop("piscine_date", UNSET))

        user_candidature = cls(
            id=id,
            user_id=user_id,
            birth_city=birth_city,
            postal_street=postal_street,
            postal_city=postal_city,
            postal_zip_code=postal_zip_code,
            postal_country=postal_country,
            contact_affiliation=contact_affiliation,
            contact_last_name=contact_last_name,
            contact_first_name=contact_first_name,
            contact_phone1=contact_phone1,
            language=language,
            created_at=created_at,
            updated_at=updated_at,
            phone=phone,
            email=email,
            pin=pin,
            phone_country_code=phone_country_code,
            hidden_phone=hidden_phone,
            birth_date=birth_date,
            gender=gender,
            zip_code=zip_code,
            country=country,
            birth_country=birth_country,
            postal_complement=postal_complement,
            contact_phone2=contact_phone2,
            max_level_memory=max_level_memory,
            max_level_logic=max_level_logic,
            other_information=other_information,
            meeting_date=meeting_date,
            piscine_date=piscine_date,
        )

        user_candidature.additional_properties = d
        return user_candidature

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

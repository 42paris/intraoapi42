from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internship_convention import InternshipConvention
    from ..models.light_user import LightUser


T = TypeVar("T", bound="Internship")


@_attrs_define
class Internship:
    """
    Attributes:
        id (int):
        administration_id (int):
        offer_id (int | None):
        language_id (int):
        state (str):
        days (str):
        user_address (str):
        user_postal (str):
        user_city (str):
        user_country (str):
        company_name (str):
        company_boss_user_first_name (str):
        company_boss_user_last_name (str):
        company_boss_user_email (str):
        company_boss_user_phone (str):
        company_user_first_name (str):
        company_user_last_name (str):
        company_user_post (str):
        company_user_email (str):
        company_user_phone (str):
        company_address (str):
        company_postal (str):
        company_city (str):
        company_country (str):
        company_siret (str):
        internship_address (str):
        internship_postal (str):
        internship_city (str):
        internship_country (str):
        contract_type (str):
        subject (str):
        start_at (datetime.datetime):
        end_at (datetime.datetime):
        duration (int):
        nb_days (int):
        nb_hours (int):
        salary (float | int):
        currency (str):
        breach_at (datetime.datetime | None):
        convention (InternshipConvention):
        convention_uri (None | str):
        user (LightUser):
        projects_user (int | None | Unset):
    """

    id: int
    administration_id: int
    offer_id: int | None
    language_id: int
    state: str
    days: str
    user_address: str
    user_postal: str
    user_city: str
    user_country: str
    company_name: str
    company_boss_user_first_name: str
    company_boss_user_last_name: str
    company_boss_user_email: str
    company_boss_user_phone: str
    company_user_first_name: str
    company_user_last_name: str
    company_user_post: str
    company_user_email: str
    company_user_phone: str
    company_address: str
    company_postal: str
    company_city: str
    company_country: str
    company_siret: str
    internship_address: str
    internship_postal: str
    internship_city: str
    internship_country: str
    contract_type: str
    subject: str
    start_at: datetime.datetime
    end_at: datetime.datetime
    duration: int
    nb_days: int
    nb_hours: int
    salary: float | int
    currency: str
    breach_at: datetime.datetime | None
    convention: InternshipConvention
    convention_uri: None | str
    user: LightUser
    projects_user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        administration_id = self.administration_id

        offer_id: int | None
        offer_id = self.offer_id

        language_id = self.language_id

        state = self.state

        days = self.days

        user_address = self.user_address

        user_postal = self.user_postal

        user_city = self.user_city

        user_country = self.user_country

        company_name = self.company_name

        company_boss_user_first_name = self.company_boss_user_first_name

        company_boss_user_last_name = self.company_boss_user_last_name

        company_boss_user_email = self.company_boss_user_email

        company_boss_user_phone = self.company_boss_user_phone

        company_user_first_name = self.company_user_first_name

        company_user_last_name = self.company_user_last_name

        company_user_post = self.company_user_post

        company_user_email = self.company_user_email

        company_user_phone = self.company_user_phone

        company_address = self.company_address

        company_postal = self.company_postal

        company_city = self.company_city

        company_country = self.company_country

        company_siret = self.company_siret

        internship_address = self.internship_address

        internship_postal = self.internship_postal

        internship_city = self.internship_city

        internship_country = self.internship_country

        contract_type = self.contract_type

        subject = self.subject

        start_at = self.start_at.isoformat()

        end_at = self.end_at.isoformat()

        duration = self.duration

        nb_days = self.nb_days

        nb_hours = self.nb_hours

        salary: float | int
        salary = self.salary

        currency = self.currency

        breach_at: None | str
        if isinstance(self.breach_at, datetime.datetime):
            breach_at = self.breach_at.isoformat()
        else:
            breach_at = self.breach_at

        convention = self.convention.to_dict()

        convention_uri: None | str
        convention_uri = self.convention_uri

        user = self.user.to_dict()

        projects_user: int | None | Unset
        if isinstance(self.projects_user, Unset):
            projects_user = UNSET
        else:
            projects_user = self.projects_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "administration_id": administration_id,
                "offer_id": offer_id,
                "language_id": language_id,
                "state": state,
                "days": days,
                "user_address": user_address,
                "user_postal": user_postal,
                "user_city": user_city,
                "user_country": user_country,
                "company_name": company_name,
                "company_boss_user_first_name": company_boss_user_first_name,
                "company_boss_user_last_name": company_boss_user_last_name,
                "company_boss_user_email": company_boss_user_email,
                "company_boss_user_phone": company_boss_user_phone,
                "company_user_first_name": company_user_first_name,
                "company_user_last_name": company_user_last_name,
                "company_user_post": company_user_post,
                "company_user_email": company_user_email,
                "company_user_phone": company_user_phone,
                "company_address": company_address,
                "company_postal": company_postal,
                "company_city": company_city,
                "company_country": company_country,
                "company_siret": company_siret,
                "internship_address": internship_address,
                "internship_postal": internship_postal,
                "internship_city": internship_city,
                "internship_country": internship_country,
                "contract_type": contract_type,
                "subject": subject,
                "start_at": start_at,
                "end_at": end_at,
                "duration": duration,
                "nb_days": nb_days,
                "nb_hours": nb_hours,
                "salary": salary,
                "currency": currency,
                "breach_at": breach_at,
                "convention": convention,
                "convention_uri": convention_uri,
                "user": user,
            }
        )
        if projects_user is not UNSET:
            field_dict["projects_user"] = projects_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internship_convention import InternshipConvention
        from ..models.light_user import LightUser

        d = dict(src_dict)
        id = d.pop("id")

        administration_id = d.pop("administration_id")

        def _parse_offer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        offer_id = _parse_offer_id(d.pop("offer_id"))

        language_id = d.pop("language_id")

        state = d.pop("state")

        days = d.pop("days")

        user_address = d.pop("user_address")

        user_postal = d.pop("user_postal")

        user_city = d.pop("user_city")

        user_country = d.pop("user_country")

        company_name = d.pop("company_name")

        company_boss_user_first_name = d.pop("company_boss_user_first_name")

        company_boss_user_last_name = d.pop("company_boss_user_last_name")

        company_boss_user_email = d.pop("company_boss_user_email")

        company_boss_user_phone = d.pop("company_boss_user_phone")

        company_user_first_name = d.pop("company_user_first_name")

        company_user_last_name = d.pop("company_user_last_name")

        company_user_post = d.pop("company_user_post")

        company_user_email = d.pop("company_user_email")

        company_user_phone = d.pop("company_user_phone")

        company_address = d.pop("company_address")

        company_postal = d.pop("company_postal")

        company_city = d.pop("company_city")

        company_country = d.pop("company_country")

        company_siret = d.pop("company_siret")

        internship_address = d.pop("internship_address")

        internship_postal = d.pop("internship_postal")

        internship_city = d.pop("internship_city")

        internship_country = d.pop("internship_country")

        contract_type = d.pop("contract_type")

        subject = d.pop("subject")

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        duration = d.pop("duration")

        nb_days = d.pop("nb_days")

        nb_hours = d.pop("nb_hours")

        def _parse_salary(data: object) -> float | int:
            return cast(float | int, data)

        salary = _parse_salary(d.pop("salary"))

        currency = d.pop("currency")

        def _parse_breach_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                breach_at_type_0 = datetime.datetime.fromisoformat(data)

                return breach_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        breach_at = _parse_breach_at(d.pop("breach_at"))

        convention = InternshipConvention.from_dict(d.pop("convention"))

        def _parse_convention_uri(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        convention_uri = _parse_convention_uri(d.pop("convention_uri"))

        user = LightUser.from_dict(d.pop("user"))

        def _parse_projects_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        projects_user = _parse_projects_user(d.pop("projects_user", UNSET))

        internship = cls(
            id=id,
            administration_id=administration_id,
            offer_id=offer_id,
            language_id=language_id,
            state=state,
            days=days,
            user_address=user_address,
            user_postal=user_postal,
            user_city=user_city,
            user_country=user_country,
            company_name=company_name,
            company_boss_user_first_name=company_boss_user_first_name,
            company_boss_user_last_name=company_boss_user_last_name,
            company_boss_user_email=company_boss_user_email,
            company_boss_user_phone=company_boss_user_phone,
            company_user_first_name=company_user_first_name,
            company_user_last_name=company_user_last_name,
            company_user_post=company_user_post,
            company_user_email=company_user_email,
            company_user_phone=company_user_phone,
            company_address=company_address,
            company_postal=company_postal,
            company_city=company_city,
            company_country=company_country,
            company_siret=company_siret,
            internship_address=internship_address,
            internship_postal=internship_postal,
            internship_city=internship_city,
            internship_country=internship_country,
            contract_type=contract_type,
            subject=subject,
            start_at=start_at,
            end_at=end_at,
            duration=duration,
            nb_days=nb_days,
            nb_hours=nb_hours,
            salary=salary,
            currency=currency,
            breach_at=breach_at,
            convention=convention,
            convention_uri=convention_uri,
            user=user,
            projects_user=projects_user,
        )

        internship.additional_properties = d
        return internship

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

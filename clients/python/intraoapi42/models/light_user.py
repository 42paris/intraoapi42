from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.light_user_kind import LightUserKind, check_light_user_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_image import UserImage


T = TypeVar("T", bound="LightUser")


@_attrs_define
class LightUser:
    """
    Attributes:
        id (int): The unique identifier of the user.
        login (str): The login name of the user.
        first_name (str): The first name of the user.
        usual_full_name (str): The usual full name of the user, usually usual_first_name or first_name + last_name.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        displayname (str): The display name of the user.
        kind (LightUserKind): The kind of user (e.g., student, admin, external).
        image (UserImage):
        staff (bool): Indicates if the user is staff.
        correction_point (int): The user's correction points.
        pool_month (str): The month of the user's pool.
        pool_year (str): The year of the user's pool.
        wallet (int): The user's wallet balance.
        anonymize_date (datetime.datetime | None): The date when user data will be anonymized.
        data_erasure_date (datetime.datetime | None): The date when user data will be erased.
        created_at (datetime.datetime): The user creation timestamp.
        updated_at (datetime.datetime): The last user update timestamp.
        alumnized_at (datetime.datetime | None): The date when the user became an alumnus.
        alumni (bool): Indicates if the user is an alumnus.
        active (bool): Indicates if the user is active.
        usual_first_name (None | str | Unset): The usual first name of the user, first_name if none.
        phone (str | Unset): The phone number of the user (always hidden).
        location (None | str | Unset): The location of the user.
    """

    id: int
    login: str
    first_name: str
    usual_full_name: str
    last_name: str
    email: str
    displayname: str
    kind: LightUserKind
    image: UserImage
    staff: bool
    correction_point: int
    pool_month: str
    pool_year: str
    wallet: int
    anonymize_date: datetime.datetime | None
    data_erasure_date: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    alumnized_at: datetime.datetime | None
    alumni: bool
    active: bool
    usual_first_name: None | str | Unset = UNSET
    phone: str | Unset = UNSET
    location: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        login = self.login

        first_name = self.first_name

        usual_full_name = self.usual_full_name

        last_name = self.last_name

        email = self.email

        displayname = self.displayname

        kind: str = self.kind

        image = self.image.to_dict()

        staff = self.staff

        correction_point = self.correction_point

        pool_month = self.pool_month

        pool_year = self.pool_year

        wallet = self.wallet

        anonymize_date: None | str
        if isinstance(self.anonymize_date, datetime.datetime):
            anonymize_date = self.anonymize_date.isoformat()
        else:
            anonymize_date = self.anonymize_date

        data_erasure_date: None | str
        if isinstance(self.data_erasure_date, datetime.datetime):
            data_erasure_date = self.data_erasure_date.isoformat()
        else:
            data_erasure_date = self.data_erasure_date

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        alumnized_at: None | str
        if isinstance(self.alumnized_at, datetime.datetime):
            alumnized_at = self.alumnized_at.isoformat()
        else:
            alumnized_at = self.alumnized_at

        alumni = self.alumni

        active = self.active

        usual_first_name: None | str | Unset
        if isinstance(self.usual_first_name, Unset):
            usual_first_name = UNSET
        else:
            usual_first_name = self.usual_first_name

        phone = self.phone

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "login": login,
                "first_name": first_name,
                "usual_full_name": usual_full_name,
                "last_name": last_name,
                "email": email,
                "displayname": displayname,
                "kind": kind,
                "image": image,
                "staff?": staff,
                "correction_point": correction_point,
                "pool_month": pool_month,
                "pool_year": pool_year,
                "wallet": wallet,
                "anonymize_date": anonymize_date,
                "data_erasure_date": data_erasure_date,
                "created_at": created_at,
                "updated_at": updated_at,
                "alumnized_at": alumnized_at,
                "alumni?": alumni,
                "active?": active,
            }
        )
        if usual_first_name is not UNSET:
            field_dict["usual_first_name"] = usual_first_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_image import UserImage

        d = dict(src_dict)
        id = d.pop("id")

        login = d.pop("login")

        first_name = d.pop("first_name")

        usual_full_name = d.pop("usual_full_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        displayname = d.pop("displayname")

        kind = check_light_user_kind(d.pop("kind"))

        image = UserImage.from_dict(d.pop("image"))

        staff = d.pop("staff?")

        correction_point = d.pop("correction_point")

        pool_month = d.pop("pool_month")

        pool_year = d.pop("pool_year")

        wallet = d.pop("wallet")

        def _parse_anonymize_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                anonymize_date_type_0 = datetime.datetime.fromisoformat(data)

                return anonymize_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        anonymize_date = _parse_anonymize_date(d.pop("anonymize_date"))

        def _parse_data_erasure_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_erasure_date_type_0 = datetime.datetime.fromisoformat(data)

                return data_erasure_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        data_erasure_date = _parse_data_erasure_date(d.pop("data_erasure_date"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_alumnized_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                alumnized_at_type_0 = datetime.datetime.fromisoformat(data)

                return alumnized_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        alumnized_at = _parse_alumnized_at(d.pop("alumnized_at"))

        alumni = d.pop("alumni?")

        active = d.pop("active?")

        def _parse_usual_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usual_first_name = _parse_usual_first_name(d.pop("usual_first_name", UNSET))

        phone = d.pop("phone", UNSET)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        light_user = cls(
            id=id,
            login=login,
            first_name=first_name,
            usual_full_name=usual_full_name,
            last_name=last_name,
            email=email,
            displayname=displayname,
            kind=kind,
            image=image,
            staff=staff,
            correction_point=correction_point,
            pool_month=pool_month,
            pool_year=pool_year,
            wallet=wallet,
            anonymize_date=anonymize_date,
            data_erasure_date=data_erasure_date,
            created_at=created_at,
            updated_at=updated_at,
            alumnized_at=alumnized_at,
            alumni=alumni,
            active=active,
            usual_first_name=usual_first_name,
            phone=phone,
            location=location,
        )

        light_user.additional_properties = d
        return light_user

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

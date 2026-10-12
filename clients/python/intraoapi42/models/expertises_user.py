from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expertise import Expertise


T = TypeVar("T", bound="ExpertisesUser")


@_attrs_define
class ExpertisesUser:
    """
    Attributes:
        id (int):
        expertise_id (int):
        user_id (int):
        interested (bool):
        contact_me (bool):
        value (int | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        expertise (Expertise | Unset):
    """

    id: int
    expertise_id: int
    user_id: int
    interested: bool
    contact_me: bool
    value: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    expertise: Expertise | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expertise_id = self.expertise_id

        user_id = self.user_id

        interested = self.interested

        contact_me = self.contact_me

        value: int | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        expertise: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expertise, Unset):
            expertise = self.expertise.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "expertise_id": expertise_id,
                "user_id": user_id,
                "interested": interested,
                "contact_me": contact_me,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if expertise is not UNSET:
            field_dict["expertise"] = expertise

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expertise import Expertise

        d = dict(src_dict)
        id = d.pop("id")

        expertise_id = d.pop("expertise_id")

        user_id = d.pop("user_id")

        interested = d.pop("interested")

        contact_me = d.pop("contact_me")

        def _parse_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _expertise = d.pop("expertise", UNSET)
        expertise: Expertise | Unset
        if isinstance(_expertise, Unset):
            expertise = UNSET
        else:
            expertise = Expertise.from_dict(_expertise)

        expertises_user = cls(
            id=id,
            expertise_id=expertise_id,
            user_id=user_id,
            interested=interested,
            contact_me=contact_me,
            value=value,
            created_at=created_at,
            updated_at=updated_at,
            expertise=expertise,
        )

        expertises_user.additional_properties = d
        return expertises_user

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

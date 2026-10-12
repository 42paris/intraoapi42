from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translation_fields import TranslationFields


T = TypeVar("T", bound="Translation")


@_attrs_define
class Translation:
    """
    Attributes:
        id (int):
        translatable_id (int):
        translatable_type (str):
        language_id (int):
        fields (TranslationFields):
        up_to_date (bool | Unset):
        default (bool | Unset):
        user_id (int | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int
    translatable_id: int
    translatable_type: str
    language_id: int
    fields: TranslationFields
    up_to_date: bool | Unset = UNSET
    default: bool | Unset = UNSET
    user_id: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        translatable_id = self.translatable_id

        translatable_type = self.translatable_type

        language_id = self.language_id

        fields = self.fields.to_dict()

        up_to_date = self.up_to_date

        default = self.default

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "translatable_id": translatable_id,
                "translatable_type": translatable_type,
                "language_id": language_id,
                "fields": fields,
            }
        )
        if up_to_date is not UNSET:
            field_dict["up_to_date"] = up_to_date
        if default is not UNSET:
            field_dict["default"] = default
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation_fields import TranslationFields

        d = dict(src_dict)
        id = d.pop("id")

        translatable_id = d.pop("translatable_id")

        translatable_type = d.pop("translatable_type")

        language_id = d.pop("language_id")

        fields = TranslationFields.from_dict(d.pop("fields"))

        up_to_date = d.pop("up_to_date", UNSET)

        default = d.pop("default", UNSET)

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

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

        translation = cls(
            id=id,
            translatable_id=translatable_id,
            translatable_type=translatable_type,
            language_id=language_id,
            fields=fields,
            up_to_date=up_to_date,
            default=default,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        translation.additional_properties = d
        return translation

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_preview import UserPreview


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """
    Attributes:
        id (int):
        begin_at (datetime.datetime):
        primary (bool):
        host (str):
        campus_id (int):
        end_at (datetime.datetime | None | Unset):
        user (UserPreview | Unset):
    """

    id: int
    begin_at: datetime.datetime
    primary: bool
    host: str
    campus_id: int
    end_at: datetime.datetime | None | Unset = UNSET
    user: UserPreview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        begin_at = self.begin_at.isoformat()

        primary = self.primary

        host = self.host

        campus_id = self.campus_id

        end_at: None | str | Unset
        if isinstance(self.end_at, Unset):
            end_at = UNSET
        elif isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "begin_at": begin_at,
                "primary": primary,
                "host": host,
                "campus_id": campus_id,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_preview import UserPreview

        d = dict(src_dict)
        id = d.pop("id")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        primary = d.pop("primary")

        host = d.pop("host")

        campus_id = d.pop("campus_id")

        def _parse_end_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = datetime.datetime.fromisoformat(data)

                return end_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_at = _parse_end_at(d.pop("end_at", UNSET))

        _user = d.pop("user", UNSET)
        user: UserPreview | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserPreview.from_dict(_user)

        location = cls(
            id=id,
            begin_at=begin_at,
            primary=primary,
            host=host,
            campus_id=campus_id,
            end_at=end_at,
            user=user,
        )

        location.additional_properties = d
        return location

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

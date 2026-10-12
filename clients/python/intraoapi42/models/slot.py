from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.light_user import LightUser


T = TypeVar("T", bound="Slot")


@_attrs_define
class Slot:
    """
    Attributes:
        id (int):
        begin_at (datetime.datetime):
        end_at (datetime.datetime):
        scale_team_id (int | None | Unset):
        user (LightUser | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: int
    begin_at: datetime.datetime
    end_at: datetime.datetime
    scale_team_id: int | None | Unset = UNSET
    user: LightUser | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        begin_at = self.begin_at.isoformat()

        end_at = self.end_at.isoformat()

        scale_team_id: int | None | Unset
        if isinstance(self.scale_team_id, Unset):
            scale_team_id = UNSET
        else:
            scale_team_id = self.scale_team_id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "begin_at": begin_at,
                "end_at": end_at,
            }
        )
        if scale_team_id is not UNSET:
            field_dict["scale_team_id"] = scale_team_id
        if user is not UNSET:
            field_dict["user"] = user
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_user import LightUser

        d = dict(src_dict)
        id = d.pop("id")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        def _parse_scale_team_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scale_team_id = _parse_scale_team_id(d.pop("scale_team_id", UNSET))

        _user = d.pop("user", UNSET)
        user: LightUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LightUser.from_dict(_user)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        slot = cls(
            id=id,
            begin_at=begin_at,
            end_at=end_at,
            scale_team_id=scale_team_id,
            user=user,
            created_at=created_at,
        )

        slot.additional_properties = d
        return slot

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlotCreateSlot")


@_attrs_define
class SlotCreateSlot:
    """
    Attributes:
        user_id (int): Must match the token owner unless Advanced tutor
        begin_at (datetime.datetime):
        end_at (datetime.datetime):
        scale_team_id (int | None | Unset): Optional defense to link to this slot
    """

    user_id: int
    begin_at: datetime.datetime
    end_at: datetime.datetime
    scale_team_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        begin_at = self.begin_at.isoformat()

        end_at = self.end_at.isoformat()

        scale_team_id: int | None | Unset
        if isinstance(self.scale_team_id, Unset):
            scale_team_id = UNSET
        else:
            scale_team_id = self.scale_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "begin_at": begin_at,
                "end_at": end_at,
            }
        )
        if scale_team_id is not UNSET:
            field_dict["scale_team_id"] = scale_team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        def _parse_scale_team_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scale_team_id = _parse_scale_team_id(d.pop("scale_team_id", UNSET))

        slot_create_slot = cls(
            user_id=user_id,
            begin_at=begin_at,
            end_at=end_at,
            scale_team_id=scale_team_id,
        )

        slot_create_slot.additional_properties = d
        return slot_create_slot

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

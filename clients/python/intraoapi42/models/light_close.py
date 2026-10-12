from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.light_close_kind import LightCloseKind, check_light_close_kind
from ..models.light_close_state import LightCloseState, check_light_close_state

T = TypeVar("T", bound="LightClose")


@_attrs_define
class LightClose:
    """
    Attributes:
        id (int):
        reason (str):
        state (LightCloseState):
        kind (LightCloseKind):
        end_at (datetime.datetime | None):
        primary_campus_id (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    reason: str
    state: LightCloseState
    kind: LightCloseKind
    end_at: datetime.datetime | None
    primary_campus_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reason = self.reason

        state: str = self.state

        kind: str = self.kind

        end_at: None | str
        if isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        primary_campus_id = self.primary_campus_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reason": reason,
                "state": state,
                "kind": kind,
                "end_at": end_at,
                "primary_campus_id": primary_campus_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        reason = d.pop("reason")

        state = check_light_close_state(d.pop("state"))

        kind = check_light_close_kind(d.pop("kind"))

        def _parse_end_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = datetime.datetime.fromisoformat(data)

                return end_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_at = _parse_end_at(d.pop("end_at"))

        primary_campus_id = d.pop("primary_campus_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        light_close = cls(
            id=id,
            reason=reason,
            state=state,
            kind=kind,
            end_at=end_at,
            primary_campus_id=primary_campus_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        light_close.additional_properties = d
        return light_close

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

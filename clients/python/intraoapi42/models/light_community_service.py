from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.light_community_service_state import LightCommunityServiceState, check_light_community_service_state

T = TypeVar("T", bound="LightCommunityService")


@_attrs_define
class LightCommunityService:
    """
    Attributes:
        id (int):
        duration (int):
        schedule_at (datetime.datetime):
        occupation (str):
        state (LightCommunityServiceState):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    duration: int
    schedule_at: datetime.datetime
    occupation: str
    state: LightCommunityServiceState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        duration = self.duration

        schedule_at = self.schedule_at.isoformat()

        occupation = self.occupation

        state: str = self.state

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "duration": duration,
                "schedule_at": schedule_at,
                "occupation": occupation,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        duration = d.pop("duration")

        schedule_at = datetime.datetime.fromisoformat(d.pop("schedule_at"))

        occupation = d.pop("occupation")

        state = check_light_community_service_state(d.pop("state"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        light_community_service = cls(
            id=id,
            duration=duration,
            schedule_at=schedule_at,
            occupation=occupation,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
        )

        light_community_service.additional_properties = d
        return light_community_service

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

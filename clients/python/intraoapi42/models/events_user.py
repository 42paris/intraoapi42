from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.events_user_event import EventsUserEvent
    from ..models.user_preview import UserPreview


T = TypeVar("T", bound="EventsUser")


@_attrs_define
class EventsUser:
    """
    Attributes:
        id (int):
        event_id (int):
        user_id (int):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        user (UserPreview | Unset):
        event (EventsUserEvent | Unset):
    """

    id: int
    event_id: int
    user_id: int
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user: UserPreview | Unset = UNSET
    event: EventsUserEvent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_id = self.event_id

        user_id = self.user_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_id": event_id,
                "user_id": user_id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.events_user_event import EventsUserEvent
        from ..models.user_preview import UserPreview

        d = dict(src_dict)
        id = d.pop("id")

        event_id = d.pop("event_id")

        user_id = d.pop("user_id")

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

        _user = d.pop("user", UNSET)
        user: UserPreview | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserPreview.from_dict(_user)

        _event = d.pop("event", UNSET)
        event: EventsUserEvent | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = EventsUserEvent.from_dict(_event)

        events_user = cls(
            id=id,
            event_id=event_id,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            user=user,
            event=event,
        )

        events_user.additional_properties = d
        return events_user

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

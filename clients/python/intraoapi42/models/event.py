from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_themes_item import EventThemesItem
    from ..models.event_waitlist_type_0 import EventWaitlistType0


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        kind (str):
        nbr_subscribers (int):
        begin_at (datetime.datetime):
        end_at (datetime.datetime):
        campus_ids (list[int]):
        cursus_ids (list[int]):
        location (None | str | Unset):
        max_people (int | None | Unset):
        themes (list[EventThemesItem] | Unset):
        waitlist (EventWaitlistType0 | None | Unset):
        difficulty (int | None | Unset):
        prohibition_of_cancellation (int | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int
    name: str
    description: str
    kind: str
    nbr_subscribers: int
    begin_at: datetime.datetime
    end_at: datetime.datetime
    campus_ids: list[int]
    cursus_ids: list[int]
    location: None | str | Unset = UNSET
    max_people: int | None | Unset = UNSET
    themes: list[EventThemesItem] | Unset = UNSET
    waitlist: EventWaitlistType0 | None | Unset = UNSET
    difficulty: int | None | Unset = UNSET
    prohibition_of_cancellation: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_waitlist_type_0 import EventWaitlistType0

        id = self.id

        name = self.name

        description = self.description

        kind = self.kind

        nbr_subscribers = self.nbr_subscribers

        begin_at = self.begin_at.isoformat()

        end_at = self.end_at.isoformat()

        campus_ids = self.campus_ids

        cursus_ids = self.cursus_ids

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        max_people: int | None | Unset
        if isinstance(self.max_people, Unset):
            max_people = UNSET
        else:
            max_people = self.max_people

        themes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.themes, Unset):
            themes = []
            for themes_item_data in self.themes:
                themes_item = themes_item_data.to_dict()
                themes.append(themes_item)

        waitlist: dict[str, Any] | None | Unset
        if isinstance(self.waitlist, Unset):
            waitlist = UNSET
        elif isinstance(self.waitlist, EventWaitlistType0):
            waitlist = self.waitlist.to_dict()
        else:
            waitlist = self.waitlist

        difficulty: int | None | Unset
        if isinstance(self.difficulty, Unset):
            difficulty = UNSET
        else:
            difficulty = self.difficulty

        prohibition_of_cancellation: int | None | Unset
        if isinstance(self.prohibition_of_cancellation, Unset):
            prohibition_of_cancellation = UNSET
        else:
            prohibition_of_cancellation = self.prohibition_of_cancellation

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
                "name": name,
                "description": description,
                "kind": kind,
                "nbr_subscribers": nbr_subscribers,
                "begin_at": begin_at,
                "end_at": end_at,
                "campus_ids": campus_ids,
                "cursus_ids": cursus_ids,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if max_people is not UNSET:
            field_dict["max_people"] = max_people
        if themes is not UNSET:
            field_dict["themes"] = themes
        if waitlist is not UNSET:
            field_dict["waitlist"] = waitlist
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if prohibition_of_cancellation is not UNSET:
            field_dict["prohibition_of_cancellation"] = prohibition_of_cancellation
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_themes_item import EventThemesItem
        from ..models.event_waitlist_type_0 import EventWaitlistType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        kind = d.pop("kind")

        nbr_subscribers = d.pop("nbr_subscribers")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        campus_ids = cast(list[int], d.pop("campus_ids"))

        cursus_ids = cast(list[int], d.pop("cursus_ids"))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_max_people(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_people = _parse_max_people(d.pop("max_people", UNSET))

        _themes = d.pop("themes", UNSET)
        themes: list[EventThemesItem] | Unset = UNSET
        if _themes is not UNSET:
            themes = []
            for themes_item_data in _themes:
                themes_item = EventThemesItem.from_dict(themes_item_data)

                themes.append(themes_item)

        def _parse_waitlist(data: object) -> EventWaitlistType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                waitlist_type_0 = EventWaitlistType0.from_dict(data)

                return waitlist_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventWaitlistType0 | None | Unset, data)

        waitlist = _parse_waitlist(d.pop("waitlist", UNSET))

        def _parse_difficulty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        difficulty = _parse_difficulty(d.pop("difficulty", UNSET))

        def _parse_prohibition_of_cancellation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prohibition_of_cancellation = _parse_prohibition_of_cancellation(d.pop("prohibition_of_cancellation", UNSET))

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

        event = cls(
            id=id,
            name=name,
            description=description,
            kind=kind,
            nbr_subscribers=nbr_subscribers,
            begin_at=begin_at,
            end_at=end_at,
            campus_ids=campus_ids,
            cursus_ids=cursus_ids,
            location=location,
            max_people=max_people,
            themes=themes,
            waitlist=waitlist,
            difficulty=difficulty,
            prohibition_of_cancellation=prohibition_of_cancellation,
            created_at=created_at,
            updated_at=updated_at,
        )

        event.additional_properties = d
        return event

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

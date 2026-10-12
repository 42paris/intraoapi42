from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.light_note_user import LightNoteUser


T = TypeVar("T", bound="LightNote")


@_attrs_define
class LightNote:
    """A comment or note left by one user about another (e.g. a scale/feedback note).

    Attributes:
        id (int): The unique identifier of this note.
        from_user (LightNoteUser): A minimal reference to a user.
        subject (str): The subject or title of the note.
        content (str): The body content of the note.
        created_at (datetime.datetime): The timestamp when the note was created.
        user (LightNoteUser): A minimal reference to a user.
    """

    id: int
    from_user: LightNoteUser
    subject: str
    content: str
    created_at: datetime.datetime
    user: LightNoteUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        from_user = self.from_user.to_dict()

        subject = self.subject

        content = self.content

        created_at = self.created_at.isoformat()

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "from_user": from_user,
                "subject": subject,
                "content": content,
                "created_at": created_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_note_user import LightNoteUser

        d = dict(src_dict)
        id = d.pop("id")

        from_user = LightNoteUser.from_dict(d.pop("from_user"))

        subject = d.pop("subject")

        content = d.pop("content")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        user = LightNoteUser.from_dict(d.pop("user"))

        light_note = cls(
            id=id,
            from_user=from_user,
            subject=subject,
            content=content,
            created_at=created_at,
            user=user,
        )

        light_note.additional_properties = d
        return light_note

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

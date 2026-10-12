from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TeamUpload")


@_attrs_define
class TeamUpload:
    """
    Attributes:
        id (int):
        final_mark (int | None):
        comment (str):
        created_at (datetime.datetime):
        upload_id (int):
    """

    id: int
    final_mark: int | None
    comment: str
    created_at: datetime.datetime
    upload_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        final_mark: int | None
        final_mark = self.final_mark

        comment = self.comment

        created_at = self.created_at.isoformat()

        upload_id = self.upload_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "final_mark": final_mark,
                "comment": comment,
                "created_at": created_at,
                "upload_id": upload_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_final_mark(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        final_mark = _parse_final_mark(d.pop("final_mark"))

        comment = d.pop("comment")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        upload_id = d.pop("upload_id")

        team_upload = cls(
            id=id,
            final_mark=final_mark,
            comment=comment,
            created_at=created_at,
            upload_id=upload_id,
        )

        team_upload.additional_properties = d
        return team_upload

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

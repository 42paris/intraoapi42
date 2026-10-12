from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CoalitionsUser")


@_attrs_define
class CoalitionsUser:
    """
    Attributes:
        id (int):
        coalition_id (int):
        user_id (int):
        score (int):
        rank (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    coalition_id: int
    user_id: int
    score: int
    rank: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        coalition_id = self.coalition_id

        user_id = self.user_id

        score = self.score

        rank = self.rank

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "coalition_id": coalition_id,
                "user_id": user_id,
                "score": score,
                "rank": rank,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        coalition_id = d.pop("coalition_id")

        user_id = d.pop("user_id")

        score = d.pop("score")

        rank = d.pop("rank")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        coalitions_user = cls(
            id=id,
            coalition_id=coalition_id,
            user_id=user_id,
            score=score,
            rank=rank,
            created_at=created_at,
            updated_at=updated_at,
        )

        coalitions_user.additional_properties = d
        return coalitions_user

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

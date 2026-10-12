from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LightAchievementsUser")


@_attrs_define
class LightAchievementsUser:
    """
    Attributes:
        id (int):
        achievement_id (int):
        user_id (int):
        login (str):
        nbr_of_success (int | None):
        url (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    achievement_id: int
    user_id: int
    login: str
    nbr_of_success: int | None
    url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        achievement_id = self.achievement_id

        user_id = self.user_id

        login = self.login

        nbr_of_success: int | None
        nbr_of_success = self.nbr_of_success

        url = self.url

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "achievement_id": achievement_id,
                "user_id": user_id,
                "login": login,
                "nbr_of_success": nbr_of_success,
                "url": url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        achievement_id = d.pop("achievement_id")

        user_id = d.pop("user_id")

        login = d.pop("login")

        def _parse_nbr_of_success(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        nbr_of_success = _parse_nbr_of_success(d.pop("nbr_of_success"))

        url = d.pop("url")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        light_achievements_user = cls(
            id=id,
            achievement_id=achievement_id,
            user_id=user_id,
            login=login,
            nbr_of_success=nbr_of_success,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
        )

        light_achievements_user.additional_properties = d
        return light_achievements_user

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

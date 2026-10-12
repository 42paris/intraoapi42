from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursus import Cursus
    from ..models.light_user import LightUser
    from ..models.skill import Skill


T = TypeVar("T", bound="CursusUser")


@_attrs_define
class CursusUser:
    """
    Attributes:
        id (int):
        begin_at (datetime.datetime):
        end_at (datetime.datetime | None):
        grade (str):
        level (float):
        skills (list[Skill]):
        cursus_id (int):
        has_coalition (bool):
        blackholed_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cursus (Cursus):
        user (LightUser | Unset):
    """

    id: int
    begin_at: datetime.datetime
    end_at: datetime.datetime | None
    grade: str
    level: float
    skills: list[Skill]
    cursus_id: int
    has_coalition: bool
    blackholed_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cursus: Cursus
    user: LightUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        begin_at = self.begin_at.isoformat()

        end_at: None | str
        if isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        grade = self.grade

        level = self.level

        skills = []
        for skills_item_data in self.skills:
            skills_item = skills_item_data.to_dict()
            skills.append(skills_item)

        cursus_id = self.cursus_id

        has_coalition = self.has_coalition

        blackholed_at: None | str
        if isinstance(self.blackholed_at, datetime.datetime):
            blackholed_at = self.blackholed_at.isoformat()
        else:
            blackholed_at = self.blackholed_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cursus = self.cursus.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "begin_at": begin_at,
                "end_at": end_at,
                "grade": grade,
                "level": level,
                "skills": skills,
                "cursus_id": cursus_id,
                "has_coalition": has_coalition,
                "blackholed_at": blackholed_at,
                "created_at": created_at,
                "updated_at": updated_at,
                "cursus": cursus,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursus import Cursus
        from ..models.light_user import LightUser
        from ..models.skill import Skill

        d = dict(src_dict)
        id = d.pop("id")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

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

        grade = d.pop("grade")

        level = d.pop("level")

        skills = []
        _skills = d.pop("skills")
        for skills_item_data in _skills:
            skills_item = Skill.from_dict(skills_item_data)

            skills.append(skills_item)

        cursus_id = d.pop("cursus_id")

        has_coalition = d.pop("has_coalition")

        def _parse_blackholed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blackholed_at_type_0 = datetime.datetime.fromisoformat(data)

                return blackholed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        blackholed_at = _parse_blackholed_at(d.pop("blackholed_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        cursus = Cursus.from_dict(d.pop("cursus"))

        _user = d.pop("user", UNSET)
        user: LightUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LightUser.from_dict(_user)

        cursus_user = cls(
            id=id,
            begin_at=begin_at,
            end_at=end_at,
            grade=grade,
            level=level,
            skills=skills,
            cursus_id=cursus_id,
            has_coalition=has_coalition,
            blackholed_at=blackholed_at,
            created_at=created_at,
            updated_at=updated_at,
            cursus=cursus,
            user=user,
        )

        cursus_user.additional_properties = d
        return cursus_user

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

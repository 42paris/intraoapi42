from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamUpdateTeamsUsersAttributesType0Item")


@_attrs_define
class TeamUpdateTeamsUsersAttributesType0Item:
    """
    Attributes:
        user_id (int): The user id. Must be unique in the scope of a given team.
        leader (bool | None | Unset): Is it leader? Default: False.
        validated (bool | None | Unset): Is it validated? Default: False.
        occurrence (int | None | Unset): The occurrence. Default: 0.
    """

    user_id: int
    leader: bool | None | Unset = False
    validated: bool | None | Unset = False
    occurrence: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        leader: bool | None | Unset
        if isinstance(self.leader, Unset):
            leader = UNSET
        else:
            leader = self.leader

        validated: bool | None | Unset
        if isinstance(self.validated, Unset):
            validated = UNSET
        else:
            validated = self.validated

        occurrence: int | None | Unset
        if isinstance(self.occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = self.occurrence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if leader is not UNSET:
            field_dict["leader"] = leader
        if validated is not UNSET:
            field_dict["validated"] = validated
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        def _parse_leader(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        leader = _parse_leader(d.pop("leader", UNSET))

        def _parse_validated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        validated = _parse_validated(d.pop("validated", UNSET))

        def _parse_occurrence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occurrence = _parse_occurrence(d.pop("occurrence", UNSET))

        team_update_teams_users_attributes_type_0_item = cls(
            user_id=user_id,
            leader=leader,
            validated=validated,
            occurrence=occurrence,
        )

        team_update_teams_users_attributes_type_0_item.additional_properties = d
        return team_update_teams_users_attributes_type_0_item

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

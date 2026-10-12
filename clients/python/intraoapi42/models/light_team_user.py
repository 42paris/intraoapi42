from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LightTeamUser")


@_attrs_define
class LightTeamUser:
    """
    Attributes:
        id (int):
        login (str):
        url (str):
        leader (bool):
        occurrence (int):
        validated (bool):
        projects_user_id (int):
    """

    id: int
    login: str
    url: str
    leader: bool
    occurrence: int
    validated: bool
    projects_user_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        login = self.login

        url = self.url

        leader = self.leader

        occurrence = self.occurrence

        validated = self.validated

        projects_user_id = self.projects_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "login": login,
                "url": url,
                "leader": leader,
                "occurrence": occurrence,
                "validated": validated,
                "projects_user_id": projects_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        login = d.pop("login")

        url = d.pop("url")

        leader = d.pop("leader")

        occurrence = d.pop("occurrence")

        validated = d.pop("validated")

        projects_user_id = d.pop("projects_user_id")

        light_team_user = cls(
            id=id,
            login=login,
            url=url,
            leader=leader,
            occurrence=occurrence,
            validated=validated,
            projects_user_id=projects_user_id,
        )

        light_team_user.additional_properties = d
        return light_team_user

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

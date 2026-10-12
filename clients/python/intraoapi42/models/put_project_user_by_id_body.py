from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_user_update import ProjectUserUpdate


T = TypeVar("T", bound="PutProjectUserByIdBody")


@_attrs_define
class PutProjectUserByIdBody:
    """
    Attributes:
        projects_user (ProjectUserUpdate):
    """

    projects_user: ProjectUserUpdate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects_user = self.projects_user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects_user": projects_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_user_update import ProjectUserUpdate

        d = dict(src_dict)
        projects_user = ProjectUserUpdate.from_dict(d.pop("projects_user"))

        put_project_user_by_id_body = cls(
            projects_user=projects_user,
        )

        put_project_user_by_id_body.additional_properties = d
        return put_project_user_by_id_body

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectProjectStatistics")


@_attrs_define
class ProjectProjectStatistics:
    """
    Attributes:
        average_mark (float | None | Unset):
        count (int | Unset):
    """

    average_mark: float | None | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_mark: float | None | Unset
        if isinstance(self.average_mark, Unset):
            average_mark = UNSET
        else:
            average_mark = self.average_mark

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_mark is not UNSET:
            field_dict["average_mark"] = average_mark
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_average_mark(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_mark = _parse_average_mark(d.pop("average_mark", UNSET))

        count = d.pop("count", UNSET)

        project_project_statistics = cls(
            average_mark=average_mark,
            count=count,
        )

        project_project_statistics.additional_properties = d
        return project_project_statistics

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.internship_convention_convention import InternshipConventionConvention


T = TypeVar("T", bound="InternshipConvention")


@_attrs_define
class InternshipConvention:
    """
    Attributes:
        convention (InternshipConventionConvention):
    """

    convention: InternshipConventionConvention
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convention = self.convention.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "convention": convention,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internship_convention_convention import InternshipConventionConvention

        d = dict(src_dict)
        convention = InternshipConventionConvention.from_dict(d.pop("convention"))

        internship_convention = cls(
            convention=convention,
        )

        internship_convention.additional_properties = d
        return internship_convention

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

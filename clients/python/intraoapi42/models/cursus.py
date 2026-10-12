from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Cursus")


@_attrs_define
class Cursus:
    """
    Attributes:
        id (int):
        created_at (datetime.datetime):
        name (str):
        slug (str):
        kind (str):
    """

    id: int
    created_at: datetime.datetime
    name: str
    slug: str
    kind: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        name = self.name

        slug = self.slug

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "name": name,
                "slug": slug,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        name = d.pop("name")

        slug = d.pop("slug")

        kind = d.pop("kind")

        cursus = cls(
            id=id,
            created_at=created_at,
            name=name,
            slug=slug,
            kind=kind,
        )

        cursus.additional_properties = d
        return cursus

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

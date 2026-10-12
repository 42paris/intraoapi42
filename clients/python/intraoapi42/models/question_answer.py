from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuestionAnswer")


@_attrs_define
class QuestionAnswer:
    """
    Attributes:
        id (int):
        value (int | None):
        answer (None | str):
    """

    id: int
    value: int | None
    answer: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value: int | None
        value = self.value

        answer: None | str
        answer = self.answer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
                "answer": answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_value(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        value = _parse_value(d.pop("value"))

        def _parse_answer(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        answer = _parse_answer(d.pop("answer"))

        question_answer = cls(
            id=id,
            value=value,
            answer=answer,
        )

        question_answer.additional_properties = d
        return question_answer

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

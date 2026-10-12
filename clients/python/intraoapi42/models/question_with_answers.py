from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.question_answer import QuestionAnswer


T = TypeVar("T", bound="QuestionWithAnswers")


@_attrs_define
class QuestionWithAnswers:
    """
    Attributes:
        id (int):
        name (str):
        guidelines (str):
        rating (str):
        kind (str):
        position (int):
        answers (list[QuestionAnswer]):
    """

    id: int
    name: str
    guidelines: str
    rating: str
    kind: str
    position: int
    answers: list[QuestionAnswer]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        guidelines = self.guidelines

        rating = self.rating

        kind = self.kind

        position = self.position

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "guidelines": guidelines,
                "rating": rating,
                "kind": kind,
                "position": position,
                "answers": answers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.question_answer import QuestionAnswer

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        guidelines = d.pop("guidelines")

        rating = d.pop("rating")

        kind = d.pop("kind")

        position = d.pop("position")

        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = QuestionAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        question_with_answers = cls(
            id=id,
            name=name,
            guidelines=guidelines,
            rating=rating,
            kind=kind,
            position=position,
            answers=answers,
        )

        question_with_answers.additional_properties = d
        return question_with_answers

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

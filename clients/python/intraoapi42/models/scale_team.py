from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_with_answers import QuestionWithAnswers
    from ..models.scale_flag import ScaleFlag
    from ..models.scale_team_truant import ScaleTeamTruant
    from ..models.scale_user import ScaleUser
    from ..models.team_upload import TeamUpload


T = TypeVar("T", bound="ScaleTeam")


@_attrs_define
class ScaleTeam:
    """
    Attributes:
        id (int):
        scale_id (int):
        comment (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        feedback (str):
        final_mark (int | None):
        flag (ScaleFlag):
        begin_at (datetime.datetime):
        correcteds (list[ScaleUser]):
        corrector (ScaleUser):
        truant (ScaleTeamTruant):
        filled_at (datetime.datetime | None):
        questions_with_answers (list[QuestionWithAnswers]):
        teams_uploads (list[TeamUpload] | Unset):
    """

    id: int
    scale_id: int
    comment: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    feedback: str
    final_mark: int | None
    flag: ScaleFlag
    begin_at: datetime.datetime
    correcteds: list[ScaleUser]
    corrector: ScaleUser
    truant: ScaleTeamTruant
    filled_at: datetime.datetime | None
    questions_with_answers: list[QuestionWithAnswers]
    teams_uploads: list[TeamUpload] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scale_id = self.scale_id

        comment = self.comment

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        feedback = self.feedback

        final_mark: int | None
        final_mark = self.final_mark

        flag = self.flag.to_dict()

        begin_at = self.begin_at.isoformat()

        correcteds = []
        for correcteds_item_data in self.correcteds:
            correcteds_item = correcteds_item_data.to_dict()
            correcteds.append(correcteds_item)

        corrector = self.corrector.to_dict()

        truant = self.truant.to_dict()

        filled_at: None | str
        if isinstance(self.filled_at, datetime.datetime):
            filled_at = self.filled_at.isoformat()
        else:
            filled_at = self.filled_at

        questions_with_answers = []
        for questions_with_answers_item_data in self.questions_with_answers:
            questions_with_answers_item = questions_with_answers_item_data.to_dict()
            questions_with_answers.append(questions_with_answers_item)

        teams_uploads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams_uploads, Unset):
            teams_uploads = []
            for teams_uploads_item_data in self.teams_uploads:
                teams_uploads_item = teams_uploads_item_data.to_dict()
                teams_uploads.append(teams_uploads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scale_id": scale_id,
                "comment": comment,
                "created_at": created_at,
                "updated_at": updated_at,
                "feedback": feedback,
                "final_mark": final_mark,
                "flag": flag,
                "begin_at": begin_at,
                "correcteds": correcteds,
                "corrector": corrector,
                "truant": truant,
                "filled_at": filled_at,
                "questions_with_answers": questions_with_answers,
            }
        )
        if teams_uploads is not UNSET:
            field_dict["teams_uploads"] = teams_uploads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.question_with_answers import QuestionWithAnswers
        from ..models.scale_flag import ScaleFlag
        from ..models.scale_team_truant import ScaleTeamTruant
        from ..models.scale_user import ScaleUser
        from ..models.team_upload import TeamUpload

        d = dict(src_dict)
        id = d.pop("id")

        scale_id = d.pop("scale_id")

        comment = d.pop("comment")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        feedback = d.pop("feedback")

        def _parse_final_mark(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        final_mark = _parse_final_mark(d.pop("final_mark"))

        flag = ScaleFlag.from_dict(d.pop("flag"))

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        correcteds = []
        _correcteds = d.pop("correcteds")
        for correcteds_item_data in _correcteds:
            correcteds_item = ScaleUser.from_dict(correcteds_item_data)

            correcteds.append(correcteds_item)

        corrector = ScaleUser.from_dict(d.pop("corrector"))

        truant = ScaleTeamTruant.from_dict(d.pop("truant"))

        def _parse_filled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filled_at_type_0 = datetime.datetime.fromisoformat(data)

                return filled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        filled_at = _parse_filled_at(d.pop("filled_at"))

        questions_with_answers = []
        _questions_with_answers = d.pop("questions_with_answers")
        for questions_with_answers_item_data in _questions_with_answers:
            questions_with_answers_item = QuestionWithAnswers.from_dict(questions_with_answers_item_data)

            questions_with_answers.append(questions_with_answers_item)

        _teams_uploads = d.pop("teams_uploads", UNSET)
        teams_uploads: list[TeamUpload] | Unset = UNSET
        if _teams_uploads is not UNSET:
            teams_uploads = []
            for teams_uploads_item_data in _teams_uploads:
                teams_uploads_item = TeamUpload.from_dict(teams_uploads_item_data)

                teams_uploads.append(teams_uploads_item)

        scale_team = cls(
            id=id,
            scale_id=scale_id,
            comment=comment,
            created_at=created_at,
            updated_at=updated_at,
            feedback=feedback,
            final_mark=final_mark,
            flag=flag,
            begin_at=begin_at,
            correcteds=correcteds,
            corrector=corrector,
            truant=truant,
            filled_at=filled_at,
            questions_with_answers=questions_with_answers,
            teams_uploads=teams_uploads,
        )

        scale_team.additional_properties = d
        return scale_team

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

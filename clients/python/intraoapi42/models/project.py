from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursus import Cursus
    from ..models.light_project import LightProject
    from ..models.project_project_statistics import ProjectProjectStatistics
    from ..models.project_tags_item import ProjectTagsItem


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        id (int):
        name (str):
        slug (str):
        exam (bool):
        description (str | Unset):
        parent (LightProject | Unset):
        children (list[LightProject] | Unset):
        objectives (list[str] | Unset):
        tags (list[ProjectTagsItem] | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        repository (None | str | Unset):
        difficulty (int | None | Unset):
        cursus (list[Cursus] | Unset):
        project_sessions_ids (list[int] | Unset):
        project_statistics (ProjectProjectStatistics | Unset):
    """

    id: int
    name: str
    slug: str
    exam: bool
    description: str | Unset = UNSET
    parent: LightProject | Unset = UNSET
    children: list[LightProject] | Unset = UNSET
    objectives: list[str] | Unset = UNSET
    tags: list[ProjectTagsItem] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    repository: None | str | Unset = UNSET
    difficulty: int | None | Unset = UNSET
    cursus: list[Cursus] | Unset = UNSET
    project_sessions_ids: list[int] | Unset = UNSET
    project_statistics: ProjectProjectStatistics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        exam = self.exam

        description = self.description

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        objectives: list[str] | Unset = UNSET
        if not isinstance(self.objectives, Unset):
            objectives = self.objectives

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        repository: None | str | Unset
        if isinstance(self.repository, Unset):
            repository = UNSET
        else:
            repository = self.repository

        difficulty: int | None | Unset
        if isinstance(self.difficulty, Unset):
            difficulty = UNSET
        else:
            difficulty = self.difficulty

        cursus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cursus, Unset):
            cursus = []
            for cursus_item_data in self.cursus:
                cursus_item = cursus_item_data.to_dict()
                cursus.append(cursus_item)

        project_sessions_ids: list[int] | Unset = UNSET
        if not isinstance(self.project_sessions_ids, Unset):
            project_sessions_ids = self.project_sessions_ids

        project_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_statistics, Unset):
            project_statistics = self.project_statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "exam": exam,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if parent is not UNSET:
            field_dict["parent"] = parent
        if children is not UNSET:
            field_dict["children"] = children
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if repository is not UNSET:
            field_dict["repository"] = repository
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if cursus is not UNSET:
            field_dict["cursus"] = cursus
        if project_sessions_ids is not UNSET:
            field_dict["project_sessions_ids"] = project_sessions_ids
        if project_statistics is not UNSET:
            field_dict["project_statistics"] = project_statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursus import Cursus
        from ..models.light_project import LightProject
        from ..models.project_project_statistics import ProjectProjectStatistics
        from ..models.project_tags_item import ProjectTagsItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        exam = d.pop("exam")

        description = d.pop("description", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: LightProject | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = LightProject.from_dict(_parent)

        _children = d.pop("children", UNSET)
        children: list[LightProject] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = LightProject.from_dict(children_item_data)

                children.append(children_item)

        objectives = cast(list[str], d.pop("objectives", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[ProjectTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = ProjectTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        def _parse_repository(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository = _parse_repository(d.pop("repository", UNSET))

        def _parse_difficulty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        difficulty = _parse_difficulty(d.pop("difficulty", UNSET))

        _cursus = d.pop("cursus", UNSET)
        cursus: list[Cursus] | Unset = UNSET
        if _cursus is not UNSET:
            cursus = []
            for cursus_item_data in _cursus:
                cursus_item = Cursus.from_dict(cursus_item_data)

                cursus.append(cursus_item)

        project_sessions_ids = cast(list[int], d.pop("project_sessions_ids", UNSET))

        _project_statistics = d.pop("project_statistics", UNSET)
        project_statistics: ProjectProjectStatistics | Unset
        if isinstance(_project_statistics, Unset):
            project_statistics = UNSET
        else:
            project_statistics = ProjectProjectStatistics.from_dict(_project_statistics)

        project = cls(
            id=id,
            name=name,
            slug=slug,
            exam=exam,
            description=description,
            parent=parent,
            children=children,
            objectives=objectives,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            repository=repository,
            difficulty=difficulty,
            cursus=cursus,
            project_sessions_ids=project_sessions_ids,
            project_statistics=project_statistics,
        )

        project.additional_properties = d
        return project

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

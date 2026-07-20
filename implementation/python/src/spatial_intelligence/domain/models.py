from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ProjectState(StrEnum):
    DRAFT = "Draft"
    MEASURED = "Measured"
    NORMALIZED = "Normalized"
    VALIDATED = "Validated"
    GEOMETRY_GENERATED = "GeometryGenerated"
    ANALYZED = "Analyzed"
    EXPORTED = "Exported"
    PUBLISHED = "Published"


@dataclass(frozen=True, slots=True)
class Wall:
    wall_id: str
    start: tuple[float, float]
    end: tuple[float, float]
    thickness_mm: float

    def __post_init__(self) -> None:
        if not self.wall_id:
            raise ValueError("wall_id must not be empty")
        if self.thickness_mm <= 0:
            raise ValueError("thickness_mm must be greater than zero")
        if self.start == self.end:
            raise ValueError("wall start and end must differ")


@dataclass(frozen=True, slots=True)
class Project:
    project_id: str
    name: str
    state: ProjectState = ProjectState.DRAFT
    walls: tuple[Wall, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.project_id:
            raise ValueError("project_id must not be empty")
        if not self.name:
            raise ValueError("name must not be empty")

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from spatial_intelligence.domain import Project


@dataclass(frozen=True, slots=True)
class ProjectRecord:
    project: Project
    revision: int
    updated_at: str

    def __post_init__(self) -> None:
        if self.revision < 1:
            raise ValueError("revision must be greater than zero")

    @classmethod
    def initial(cls, project: Project) -> "ProjectRecord":
        return cls(
            project=project,
            revision=1,
            updated_at=datetime.now(UTC).isoformat(),
        )

    def next_revision(self, project: Project) -> "ProjectRecord":
        return ProjectRecord(
            project=project,
            revision=self.revision + 1,
            updated_at=datetime.now(UTC).isoformat(),
        )

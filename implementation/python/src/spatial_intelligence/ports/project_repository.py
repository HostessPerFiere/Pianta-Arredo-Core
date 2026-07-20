from __future__ import annotations

from typing import Protocol

from spatial_intelligence.persistence import ProjectRecord


class ProjectRepositoryPort(Protocol):
    def save(
        self,
        record: ProjectRecord,
        expected_revision: int | None = None,
    ) -> ProjectRecord:
        ...

    def load(self, project_id: str) -> ProjectRecord | None:
        ...

    def exists(self, project_id: str) -> bool:
        ...

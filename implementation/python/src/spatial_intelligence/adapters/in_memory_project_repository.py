from __future__ import annotations

from spatial_intelligence.persistence import ProjectRecord


class RevisionConflictError(RuntimeError):
    pass


class InMemoryProjectRepository:
    def __init__(self) -> None:
        self._records: dict[str, ProjectRecord] = {}

    def save(
        self,
        record: ProjectRecord,
        expected_revision: int | None = None,
    ) -> ProjectRecord:
        project_id = record.project.project_id
        current = self._records.get(project_id)

        if current is None:
            if expected_revision not in (None, 0):
                raise RevisionConflictError(
                    "Project does not yet have the expected revision"
                )

            self._records[project_id] = record
            return record

        if (
            expected_revision is not None
            and current.revision != expected_revision
        ):
            raise RevisionConflictError(
                f"Expected revision {expected_revision}, "
                f"found {current.revision}"
            )

        updated = current.next_revision(record.project)
        self._records[project_id] = updated
        return updated

    def load(self, project_id: str) -> ProjectRecord | None:
        return self._records.get(project_id)

    def exists(self, project_id: str) -> bool:
        return project_id in self._records

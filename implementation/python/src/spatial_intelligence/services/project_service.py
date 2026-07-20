from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import (
    ErrorCode,
    OperationResult,
    ServiceError,
)
from spatial_intelligence.domain import Project
from spatial_intelligence.persistence import ProjectRecord
from spatial_intelligence.ports.project_repository import (
    ProjectRepositoryPort,
)


class ProjectService:
    def __init__(
        self,
        repository: ProjectRepositoryPort,
    ) -> None:
        self._repository = repository

    def save_project(
        self,
        project: Project,
        expected_revision: int | None = None,
    ) -> OperationResult[ProjectRecord]:
        operation_id = str(uuid4())

        try:
            existing = self._repository.load(project.project_id)

            if existing is None:
                record = ProjectRecord.initial(project)
            else:
                record = ProjectRecord(
                    project=project,
                    revision=existing.revision,
                    updated_at=existing.updated_at,
                )

            stored = self._repository.save(
                record,
                expected_revision=expected_revision,
            )

            return OperationResult.ok(
                operation_id=operation_id,
                data=stored,
            )

        except RuntimeError as error:
            return OperationResult.fail(
                operation_id,
                ServiceError(
                    code=ErrorCode.REVISION_CONFLICT,
                    message=str(error),
                    recoverable=True,
                    subject_id=project.project_id,
                    suggested_action=(
                        "Reload the latest revision and retry."
                    ),
                ),
            )

    def load_project(
        self,
        project_id: str,
    ) -> OperationResult[ProjectRecord]:
        operation_id = str(uuid4())
        record = self._repository.load(project_id)

        if record is None:
            return OperationResult.fail(
                operation_id,
                ServiceError(
                    code=ErrorCode.ENTITY_NOT_FOUND,
                    message="Project was not found.",
                    recoverable=True,
                    subject_id=project_id,
                ),
            )

        return OperationResult.ok(
            operation_id=operation_id,
            data=record,
        )

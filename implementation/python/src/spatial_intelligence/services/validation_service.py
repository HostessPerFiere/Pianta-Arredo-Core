from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import (
    ErrorCode,
    OperationResult,
    ServiceError,
)
from spatial_intelligence.domain import Project
from spatial_intelligence.ports import KnowledgePort


class ValidationService:
    def __init__(self, knowledge_port: KnowledgePort) -> None:
        self._knowledge_port = knowledge_port

    def validate_project(
        self,
        project: Project,
    ) -> OperationResult[Project]:
        operation_id = str(uuid4())
        minimum = self._knowledge_port.minimum_wall_thickness_mm()

        errors = tuple(
            ServiceError(
                code=ErrorCode.VALIDATION_FAILED,
                message=(
                    f"Wall thickness {wall.thickness_mm} mm is below "
                    f"the configured minimum {minimum} mm."
                ),
                recoverable=True,
                subject_id=wall.wall_id,
                suggested_action="Increase Wall thickness.",
            )
            for wall in project.walls
            if wall.thickness_mm < minimum
        )

        if errors:
            return OperationResult.fail(operation_id, *errors)

        return OperationResult.ok(
            operation_id=operation_id,
            data=project,
        )

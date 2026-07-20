from __future__ import annotations

from dataclasses import replace
from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.domain import Project, ProjectState
from spatial_intelligence.ports import EventBusPort
from spatial_intelligence.services.export_service import ExportService
from spatial_intelligence.services.validation_service import ValidationService


class WorkflowService:
    def __init__(
        self,
        validation_service: ValidationService,
        export_service: ExportService,
        event_bus: EventBusPort,
    ) -> None:
        self._validation_service = validation_service
        self._export_service = export_service
        self._event_bus = event_bus

    def validate_and_export(
        self,
        project: Project,
    ) -> OperationResult[str]:
        validation = self._validation_service.validate_project(project)

        if not validation.success:
            return OperationResult(
                operation_id=str(uuid4()),
                success=False,
                errors=validation.errors,
            )

        validated_project = replace(
            project,
            state=ProjectState.VALIDATED,
        )

        export = self._export_service.export_project(validated_project)

        if not export.success or export.data is None:
            return export

        event_id = self._event_bus.publish(
            "ExportCompleted",
            {
                "projectId": project.project_id,
                "state": validated_project.state.value,
            },
        )

        return OperationResult.ok(
            operation_id=str(uuid4()),
            data=export.data,
            event_ids=(event_id,),
        )

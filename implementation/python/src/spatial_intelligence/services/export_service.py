from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.domain import Project
from spatial_intelligence.ports import ExportPort


class ExportService:
    def __init__(self, export_port: ExportPort) -> None:
        self._export_port = export_port

    def export_project(
        self,
        project: Project,
    ) -> OperationResult[str]:
        artifact = self._export_port.export_project(project)

        return OperationResult.ok(
            operation_id=str(uuid4()),
            data=artifact,
        )

from __future__ import annotations

from dataclasses import dataclass

from spatial_intelligence.adapters import (
    InMemoryEventBus,
    JsonExportAdapter,
    SimpleGeometryKernel,
    StaticKnowledgeAdapter,
)
from spatial_intelligence.services import (
    ExportService,
    GeometryService,
    KnowledgeService,
    ValidationService,
    WorkflowService,
)


@dataclass(frozen=True, slots=True)
class ApplicationServices:
    geometry: GeometryService
    knowledge: KnowledgeService
    validation: ValidationService
    export: ExportService
    workflow: WorkflowService
    event_bus: InMemoryEventBus


def build_application() -> ApplicationServices:
    geometry_kernel = SimpleGeometryKernel()
    knowledge_adapter = StaticKnowledgeAdapter()
    export_adapter = JsonExportAdapter()
    event_bus = InMemoryEventBus()

    geometry = GeometryService(geometry_kernel)
    knowledge = KnowledgeService(knowledge_adapter)
    validation = ValidationService(knowledge_adapter)
    export = ExportService(export_adapter)
    workflow = WorkflowService(
        validation_service=validation,
        export_service=export,
        event_bus=event_bus,
    )

    return ApplicationServices(
        geometry=geometry,
        knowledge=knowledge,
        validation=validation,
        export=export,
        workflow=workflow,
        event_bus=event_bus,
    )

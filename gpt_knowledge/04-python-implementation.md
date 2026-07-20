# Pianta-Arredo-Core — 04-python-implementation.md

Documento consolidato per il GPT.

---

## File originale: `implementation/python/.pytest_cache/README.md`

# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.


---

## File originale: `implementation/python/README.md`

# Python

Reserved Python implementation.


---

## File originale: `implementation/python/pyproject.toml`

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "spatial-intelligence-reference"
version = "1.0.0"
description = "Reference architecture for Pianta-Arredo-Core"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "ruff>=0.6",
  "mypy>=1.10"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.mypy]
python_version = "3.11"
strict = true
files = ["src"]


---

## File originale: `implementation/python/src/spatial_intelligence/__init__.py`

"""Spatial Intelligence reference architecture."""

__version__ = "1.0.0"


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/__init__.py`

"""Reference in-memory and JSON Adapters."""

from .in_memory_event_bus import InMemoryEventBus
from .json_export_adapter import JsonExportAdapter
from .simple_geometry_kernel import SimpleGeometryKernel
from .static_knowledge_adapter import StaticKnowledgeAdapter

__all__ = [
    "InMemoryEventBus",
    "JsonExportAdapter",
    "SimpleGeometryKernel",
    "StaticKnowledgeAdapter",
]


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/in_memory_event_bus.py`

from __future__ import annotations

from collections.abc import Mapping
from uuid import uuid4


class InMemoryEventBus:
    def __init__(self) -> None:
        self.events: list[dict[str, object]] = []

    def publish(
        self,
        event_type: str,
        payload: Mapping[str, object],
    ) -> str:
        event_id = str(uuid4())

        self.events.append(
            {
                "eventId": event_id,
                "eventType": event_type,
                "payload": dict(payload),
            }
        )

        return event_id


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/in_memory_project_repository.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/json_export_adapter.py`

from __future__ import annotations

import json
from dataclasses import asdict

from spatial_intelligence.domain import Project


class JsonExportAdapter:
    def export_project(self, project: Project) -> str:
        payload = asdict(project)
        payload["state"] = project.state.value

        return json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
        )


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/json_project_repository.py`

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from spatial_intelligence.domain import Project, ProjectState, Wall
from spatial_intelligence.persistence import ProjectRecord

from .in_memory_project_repository import RevisionConflictError


class JsonProjectRepository:
    def __init__(self, directory: Path) -> None:
        self._directory = directory
        self._directory.mkdir(parents=True, exist_ok=True)

    def _path(self, project_id: str) -> Path:
        return self._directory / f"{project_id}.json"

    def save(
        self,
        record: ProjectRecord,
        expected_revision: int | None = None,
    ) -> ProjectRecord:
        current = self.load(record.project.project_id)

        if current is None:
            if expected_revision not in (None, 0):
                raise RevisionConflictError(
                    "Project does not yet have the expected revision"
                )

            stored = record
        else:
            if (
                expected_revision is not None
                and current.revision != expected_revision
            ):
                raise RevisionConflictError(
                    f"Expected revision {expected_revision}, "
                    f"found {current.revision}"
                )

            stored = current.next_revision(record.project)

        payload = asdict(stored)
        payload["project"]["state"] = stored.project.state.value

        self._path(stored.project.project_id).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        return stored

    def load(self, project_id: str) -> ProjectRecord | None:
        path = self._path(project_id)

        if not path.exists():
            return None

        payload = json.loads(path.read_text(encoding="utf-8"))
        project_data = payload["project"]

        walls = tuple(
            Wall(
                wall_id=item["wall_id"],
                start=tuple(item["start"]),
                end=tuple(item["end"]),
                thickness_mm=item["thickness_mm"],
            )
            for item in project_data.get("walls", [])
        )

        project = Project(
            project_id=project_data["project_id"],
            name=project_data["name"],
            state=ProjectState(project_data["state"]),
            walls=walls,
        )

        return ProjectRecord(
            project=project,
            revision=payload["revision"],
            updated_at=payload["updated_at"],
        )

    def exists(self, project_id: str) -> bool:
        return self._path(project_id).exists()


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/simple_geometry_kernel.py`

from __future__ import annotations

from math import hypot

from spatial_intelligence.domain import Wall


class SimpleGeometryKernel:
    def wall_length_mm(self, wall: Wall) -> float:
        return hypot(
            wall.end[0] - wall.start[0],
            wall.end[1] - wall.start[1],
        )


---

## File originale: `implementation/python/src/spatial_intelligence/adapters/static_knowledge_adapter.py`

from __future__ import annotations


class StaticKnowledgeAdapter:
    def __init__(self, minimum_thickness_mm: float = 80.0) -> None:
        if minimum_thickness_mm <= 0:
            raise ValueError("minimum_thickness_mm must be positive")

        self._minimum_thickness_mm = minimum_thickness_mm

    def minimum_wall_thickness_mm(self) -> float:
        return self._minimum_thickness_mm


---

## File originale: `implementation/python/src/spatial_intelligence/analysis/__init__.py`

"""Deterministic spatial analysis utilities."""

from .clearance import (
    AxisAlignedBox,
    clearance_between,
    has_minimum_clearance,
)

__all__ = [
    "AxisAlignedBox",
    "clearance_between",
    "has_minimum_clearance",
]


---

## File originale: `implementation/python/src/spatial_intelligence/analysis/clearance.py`

from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True, slots=True)
class AxisAlignedBox:
    minimum_x: float
    minimum_y: float
    maximum_x: float
    maximum_y: float

    def __post_init__(self) -> None:
        if self.maximum_x <= self.minimum_x:
            raise ValueError(
                "maximum_x must exceed minimum_x"
            )

        if self.maximum_y <= self.minimum_y:
            raise ValueError(
                "maximum_y must exceed minimum_y"
            )


def clearance_between(
    first: AxisAlignedBox,
    second: AxisAlignedBox,
) -> float:
    horizontal = max(
        first.minimum_x - second.maximum_x,
        second.minimum_x - first.maximum_x,
        0.0,
    )

    vertical = max(
        first.minimum_y - second.maximum_y,
        second.minimum_y - first.maximum_y,
        0.0,
    )

    return hypot(horizontal, vertical)


def has_minimum_clearance(
    first: AxisAlignedBox,
    second: AxisAlignedBox,
    minimum_clearance: float,
) -> bool:
    if minimum_clearance < 0:
        raise ValueError(
            "minimum_clearance must not be negative"
        )

    return (
        clearance_between(first, second)
        >= minimum_clearance
    )


---

## File originale: `implementation/python/src/spatial_intelligence/api/__init__.py`

"""Stable public application facade."""

from .facade import SpatialIntelligenceApp

__all__ = ["SpatialIntelligenceApp"]


---

## File originale: `implementation/python/src/spatial_intelligence/api/facade.py`

from __future__ import annotations

from spatial_intelligence.capabilities import (
    Capability,
    build_default_registry,
)
from spatial_intelligence.composition import (
    ApplicationServices,
    build_application,
)
from spatial_intelligence.config import RuntimeSettings
from spatial_intelligence.health import (
    HealthService,
    HealthStatus,
)


class SpatialIntelligenceApp:
    def __init__(
        self,
        settings: RuntimeSettings | None = None,
    ) -> None:
        self._settings = (
            settings
            if settings is not None
            else RuntimeSettings.from_environment()
        )
        self._services = build_application()
        self._capabilities = build_default_registry()
        self._health = HealthService(
            version="1.0.0",
            settings=self._settings,
        )

    @property
    def services(self) -> ApplicationServices:
        return self._services

    def health(self) -> HealthStatus:
        return self._health.check()

    def capabilities(self) -> tuple[Capability, ...]:
        return self._capabilities.list_all()


---

## File originale: `implementation/python/src/spatial_intelligence/capabilities/__init__.py`

"""Capability declaration and discovery."""

from .registry import (
    Capability,
    CapabilityRegistry,
    build_default_registry,
)

__all__ = [
    "Capability",
    "CapabilityRegistry",
    "build_default_registry",
]


---

## File originale: `implementation/python/src/spatial_intelligence/capabilities/registry.py`

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Capability:
    capability_id: str
    version: str
    description: str


class CapabilityRegistry:
    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        existing = self._capabilities.get(
            capability.capability_id
        )

        if existing is not None and existing != capability:
            raise ValueError(
                "Capability already registered with "
                "different metadata"
            )

        self._capabilities[
            capability.capability_id
        ] = capability

    def supports(self, capability_id: str) -> bool:
        return capability_id in self._capabilities

    def get(self, capability_id: str) -> Capability | None:
        return self._capabilities.get(capability_id)

    def list_all(self) -> tuple[Capability, ...]:
        return tuple(
            sorted(
                self._capabilities.values(),
                key=lambda capability: capability.capability_id,
            )
        )


def build_default_registry() -> CapabilityRegistry:
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            capability_id="geometry.polyline-2d",
            version="0.4",
            description=(
                "Two-dimensional Point, Segment and Polyline support."
            ),
        )
    )

    registry.register(
        Capability(
            capability_id="geometry.perimeter-validation",
            version="0.4",
            description=(
                "Closed-perimeter and self-intersection validation."
            ),
        )
    )

    registry.register(
        Capability(
            capability_id="validation.opening-host",
            version="0.4",
            description=(
                "Opening placement validation against host length."
            ),
        )
    )

    return registry


---

## File originale: `implementation/python/src/spatial_intelligence/composition/__init__.py`

"""Application composition root."""

from .root import ApplicationServices, build_application

__all__ = ["ApplicationServices", "build_application"]


---

## File originale: `implementation/python/src/spatial_intelligence/composition/root.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/config/__init__.py`

"""Runtime configuration."""

from .settings import RuntimeSettings

__all__ = ["RuntimeSettings"]


---

## File originale: `implementation/python/src/spatial_intelligence/config/settings.py`

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeSettings:
    environment: str = "development"
    log_level: str = "INFO"
    data_directory: str = "./data"

    @classmethod
    def from_environment(cls) -> "RuntimeSettings":
        return cls(
            environment=os.getenv(
                "SPATIAL_ENVIRONMENT",
                "development",
            ),
            log_level=os.getenv(
                "SPATIAL_LOG_LEVEL",
                "INFO",
            ).upper(),
            data_directory=os.getenv(
                "SPATIAL_DATA_DIRECTORY",
                "./data",
            ),
        )


---

## File originale: `implementation/python/src/spatial_intelligence/contracts/__init__.py`

"""Public request, result and error contracts."""

from .errors import ErrorCode, ServiceError
from .results import OperationResult

__all__ = ["ErrorCode", "OperationResult", "ServiceError"]


---

## File originale: `implementation/python/src/spatial_intelligence/contracts/errors.py`

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ErrorCode(StrEnum):
    INVALID_REQUEST = "InvalidRequest"
    ENTITY_NOT_FOUND = "EntityNotFound"
    VALIDATION_FAILED = "ValidationFailed"
    REVISION_CONFLICT = "RevisionConflict"
    CAPABILITY_NOT_SUPPORTED = "CapabilityNotSupported"
    INTERNAL_FAILURE = "InternalFailure"


@dataclass(frozen=True, slots=True)
class ServiceError:
    code: ErrorCode
    message: str
    recoverable: bool
    subject_id: str | None = None
    suggested_action: str | None = None


---

## File originale: `implementation/python/src/spatial_intelligence/contracts/results.py`

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

from .errors import ServiceError

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class OperationResult(Generic[T]):
    operation_id: str
    success: bool
    data: T | None = None
    errors: tuple[ServiceError, ...] = field(default_factory=tuple)
    warnings: tuple[ServiceError, ...] = field(default_factory=tuple)
    event_ids: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def ok(
        cls,
        operation_id: str,
        data: T,
        event_ids: tuple[str, ...] = (),
    ) -> "OperationResult[T]":
        return cls(
            operation_id=operation_id,
            success=True,
            data=data,
            event_ids=event_ids,
        )

    @classmethod
    def fail(
        cls,
        operation_id: str,
        *errors: ServiceError,
    ) -> "OperationResult[T]":
        return cls(
            operation_id=operation_id,
            success=False,
            errors=tuple(errors),
        )


---

## File originale: `implementation/python/src/spatial_intelligence/domain/__init__.py`

"""Public domain model types."""

from .models import Project, ProjectState, Wall

__all__ = ["Project", "ProjectState", "Wall"]


---

## File originale: `implementation/python/src/spatial_intelligence/domain/models.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/events/__init__.py`

"""In-process Event infrastructure."""

from .dispatcher import Event, EventDispatcher

__all__ = ["Event", "EventDispatcher"]


---

## File originale: `implementation/python/src/spatial_intelligence/events/dispatcher.py`

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    event_type: str
    payload: Mapping[str, object]

    @classmethod
    def create(
        cls,
        event_type: str,
        payload: Mapping[str, object],
    ) -> "Event":
        if not event_type:
            raise ValueError(
                "event_type must not be empty"
            )

        return cls(
            event_id=str(uuid4()),
            event_type=event_type,
            payload=dict(payload),
        )


EventHandler = Callable[[Event], None]


class EventDispatcher:
    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[EventHandler],
        ] = {}

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        self._handlers.setdefault(
            event_type,
            [],
        ).append(handler)

    def dispatch(self, event: Event) -> None:
        for handler in self._handlers.get(
            event.event_type,
            [],
        ):
            handler(event)


---

## File originale: `implementation/python/src/spatial_intelligence/geometry/__init__.py`

"""Technology-neutral two-dimensional geometry utilities."""

from .algorithms import (
    closed_polyline_area,
    is_closed,
    polyline_length,
    segments_intersect,
    signed_area,
)
from .primitives import Point2D, Polyline2D, Segment2D

__all__ = [
    "Point2D",
    "Polyline2D",
    "Segment2D",
    "closed_polyline_area",
    "is_closed",
    "polyline_length",
    "segments_intersect",
    "signed_area",
]


---

## File originale: `implementation/python/src/spatial_intelligence/geometry/algorithms.py`

from __future__ import annotations

from math import isclose

from .primitives import Point2D, Polyline2D, Segment2D


def polyline_length(polyline: Polyline2D) -> float:
    return sum(segment.length for segment in polyline.segments)


def is_closed(
    polyline: Polyline2D,
    tolerance: float = 1e-9,
) -> bool:
    first = polyline.points[0]
    last = polyline.points[-1]

    return (
        isclose(first.x, last.x, abs_tol=tolerance)
        and isclose(first.y, last.y, abs_tol=tolerance)
    )


def signed_area(polyline: Polyline2D) -> float:
    if not is_closed(polyline):
        raise ValueError("Area requires a closed Polyline2D")

    total = 0.0

    for current, following in zip(
        polyline.points,
        polyline.points[1:],
    ):
        total += (
            current.x * following.y
            - following.x * current.y
        )

    return total / 2.0


def closed_polyline_area(polyline: Polyline2D) -> float:
    return abs(signed_area(polyline))


def _orientation(
    first: Point2D,
    second: Point2D,
    third: Point2D,
    tolerance: float,
) -> int:
    value = (
        (second.y - first.y) * (third.x - second.x)
        - (second.x - first.x) * (third.y - second.y)
    )

    if isclose(value, 0.0, abs_tol=tolerance):
        return 0

    return 1 if value > 0 else 2


def _on_segment(
    first: Point2D,
    point: Point2D,
    second: Point2D,
    tolerance: float,
) -> bool:
    return (
        min(first.x, second.x) - tolerance
        <= point.x
        <= max(first.x, second.x) + tolerance
        and min(first.y, second.y) - tolerance
        <= point.y
        <= max(first.y, second.y) + tolerance
    )


def segments_intersect(
    first: Segment2D,
    second: Segment2D,
    tolerance: float = 1e-9,
) -> bool:
    p1 = first.start
    q1 = first.end
    p2 = second.start
    q2 = second.end

    o1 = _orientation(p1, q1, p2, tolerance)
    o2 = _orientation(p1, q1, q2, tolerance)
    o3 = _orientation(p2, q2, p1, tolerance)
    o4 = _orientation(p2, q2, q1, tolerance)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and _on_segment(p1, p2, q1, tolerance):
        return True

    if o2 == 0 and _on_segment(p1, q2, q1, tolerance):
        return True

    if o3 == 0 and _on_segment(p2, p1, q2, tolerance):
        return True

    if o4 == 0 and _on_segment(p2, q1, q2, tolerance):
        return True

    return False


---

## File originale: `implementation/python/src/spatial_intelligence/geometry/primitives.py`

from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True, slots=True)
class Point2D:
    x: float
    y: float

    def distance_to(self, other: "Point2D") -> float:
        return hypot(other.x - self.x, other.y - self.y)


@dataclass(frozen=True, slots=True)
class Segment2D:
    start: Point2D
    end: Point2D

    def __post_init__(self) -> None:
        if self.start == self.end:
            raise ValueError("A Segment2D requires two different points")

    @property
    def length(self) -> float:
        return self.start.distance_to(self.end)


@dataclass(frozen=True, slots=True)
class Polyline2D:
    points: tuple[Point2D, ...]

    def __post_init__(self) -> None:
        if len(self.points) < 2:
            raise ValueError("A Polyline2D requires at least two points")

    @property
    def segments(self) -> tuple[Segment2D, ...]:
        return tuple(
            Segment2D(start, end)
            for start, end in zip(self.points, self.points[1:])
        )


---

## File originale: `implementation/python/src/spatial_intelligence/health/__init__.py`

"""Runtime health reporting."""

from .status import HealthService, HealthStatus

__all__ = ["HealthService", "HealthStatus"]


---

## File originale: `implementation/python/src/spatial_intelligence/health/status.py`

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from spatial_intelligence.config import RuntimeSettings


@dataclass(frozen=True, slots=True)
class HealthStatus:
    status: str
    version: str
    environment: str
    checked_at: str


class HealthService:
    def __init__(
        self,
        version: str,
        settings: RuntimeSettings,
    ) -> None:
        self._version = version
        self._settings = settings

    def check(self) -> HealthStatus:
        return HealthStatus(
            status="healthy",
            version=self._version,
            environment=self._settings.environment,
            checked_at=datetime.now(UTC).isoformat(),
        )


---

## File originale: `implementation/python/src/spatial_intelligence/interoperability/__init__.py`

"""Technology-neutral interoperability utilities."""

from .geojson import (
    GeoJsonError,
    export_project_geojson,
    import_walls_geojson,
)

__all__ = [
    "GeoJsonError",
    "export_project_geojson",
    "import_walls_geojson",
]


---

## File originale: `implementation/python/src/spatial_intelligence/interoperability/geojson.py`

from __future__ import annotations

import json
from typing import Any

from spatial_intelligence.domain import Project, Wall


class GeoJsonError(ValueError):
    pass


def export_project_geojson(project: Project) -> str:
    features = []

    for wall in project.walls:
        features.append(
            {
                "type": "Feature",
                "id": wall.wall_id,
                "properties": {
                    "entityType": "Wall",
                    "thicknessMm": wall.thickness_mm,
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        list(wall.start),
                        list(wall.end),
                    ],
                },
            }
        )

    payload = {
        "type": "FeatureCollection",
        "properties": {
            "projectId": project.project_id,
            "projectName": project.name,
        },
        "features": features,
    }

    return json.dumps(
        payload,
        indent=2,
        ensure_ascii=False,
    )


def import_walls_geojson(payload: str) -> tuple[Wall, ...]:
    try:
        document: dict[str, Any] = json.loads(payload)
    except json.JSONDecodeError as error:
        raise GeoJsonError("Invalid JSON payload") from error

    if document.get("type") != "FeatureCollection":
        raise GeoJsonError(
            "GeoJSON root must be a FeatureCollection"
        )

    walls: list[Wall] = []

    for feature in document.get("features", []):
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        if properties.get("entityType") != "Wall":
            continue

        if geometry.get("type") != "LineString":
            raise GeoJsonError(
                "Wall geometry must be a LineString"
            )

        coordinates = geometry.get("coordinates", [])

        if len(coordinates) != 2:
            raise GeoJsonError(
                "Wall LineString requires two coordinates"
            )

        start = coordinates[0]
        end = coordinates[1]

        walls.append(
            Wall(
                wall_id=str(feature.get("id", "")),
                start=(float(start[0]), float(start[1])),
                end=(float(end[0]), float(end[1])),
                thickness_mm=float(
                    properties["thicknessMm"]
                ),
            )
        )

    return tuple(walls)


---

## File originale: `implementation/python/src/spatial_intelligence/persistence/__init__.py`

"""Project persistence contracts and records."""

from .records import ProjectRecord

__all__ = ["ProjectRecord"]


---

## File originale: `implementation/python/src/spatial_intelligence/persistence/records.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/plugins/__init__.py`

"""Plugin registration contracts."""

from .registry import PluginDescriptor, PluginRegistry

__all__ = ["PluginDescriptor", "PluginRegistry"]


---

## File originale: `implementation/python/src/spatial_intelligence/plugins/registry.py`

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PluginDescriptor:
    plugin_id: str
    version: str
    capabilities: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.plugin_id:
            raise ValueError(
                "plugin_id must not be empty"
            )


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[
            str,
            PluginDescriptor,
        ] = {}

    def register(
        self,
        descriptor: PluginDescriptor,
    ) -> None:
        if descriptor.plugin_id in self._plugins:
            raise ValueError(
                "Plugin is already registered"
            )

        self._plugins[
            descriptor.plugin_id
        ] = descriptor

    def get(
        self,
        plugin_id: str,
    ) -> PluginDescriptor | None:
        return self._plugins.get(plugin_id)

    def supports(
        self,
        capability_id: str,
    ) -> bool:
        return any(
            capability_id in plugin.capabilities
            for plugin in self._plugins.values()
        )

    def list_all(
        self,
    ) -> tuple[PluginDescriptor, ...]:
        return tuple(
            sorted(
                self._plugins.values(),
                key=lambda plugin: plugin.plugin_id,
            )
        )


---

## File originale: `implementation/python/src/spatial_intelligence/ports/__init__.py`

"""Technology-neutral Ports."""

from .event_bus import EventBusPort
from .export import ExportPort
from .geometry import GeometryPort
from .knowledge import KnowledgePort
from .project_repository import ProjectRepositoryPort

__all__ = [
    "EventBusPort",
    "ExportPort",
    "GeometryPort",
    "KnowledgePort",
]


---

## File originale: `implementation/python/src/spatial_intelligence/ports/event_bus.py`

from __future__ import annotations

from typing import Mapping, Protocol


class EventBusPort(Protocol):
    def publish(self, event_type: str, payload: Mapping[str, object]) -> str:
        """Publish an Event and return its identifier."""
        ...


---

## File originale: `implementation/python/src/spatial_intelligence/ports/export.py`

from __future__ import annotations

from typing import Protocol

from spatial_intelligence.domain import Project


class ExportPort(Protocol):
    def export_project(self, project: Project) -> str:
        """Return a serialised export artifact."""
        ...


---

## File originale: `implementation/python/src/spatial_intelligence/ports/geometry.py`

from __future__ import annotations

from typing import Protocol

from spatial_intelligence.domain import Wall


class GeometryPort(Protocol):
    def wall_length_mm(self, wall: Wall) -> float:
        """Return Wall length in millimetres."""
        ...


---

## File originale: `implementation/python/src/spatial_intelligence/ports/knowledge.py`

from __future__ import annotations

from typing import Protocol


class KnowledgePort(Protocol):
    def minimum_wall_thickness_mm(self) -> float:
        """Return the configured minimum Wall thickness."""
        ...


---

## File originale: `implementation/python/src/spatial_intelligence/ports/project_repository.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/services/__init__.py`

"""Reference Service implementations."""

from .export_service import ExportService
from .geometry_service import GeometryService
from .knowledge_service import KnowledgeService
from .project_service import ProjectService
from .validation_service import ValidationService
from .workflow_service import WorkflowService

__all__ = [
    "ExportService",
    "GeometryService",
    "KnowledgeService",
    "ValidationService",
    "WorkflowService",
]


---

## File originale: `implementation/python/src/spatial_intelligence/services/export_service.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/services/geometry_service.py`

from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.domain import Wall
from spatial_intelligence.ports import GeometryPort


class GeometryService:
    def __init__(self, geometry_port: GeometryPort) -> None:
        self._geometry_port = geometry_port

    def calculate_wall_length(
        self,
        wall: Wall,
    ) -> OperationResult[float]:
        operation_id = str(uuid4())
        length = self._geometry_port.wall_length_mm(wall)

        return OperationResult.ok(
            operation_id=operation_id,
            data=length,
        )


---

## File originale: `implementation/python/src/spatial_intelligence/services/knowledge_service.py`

from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.ports import KnowledgePort


class KnowledgeService:
    def __init__(self, knowledge_port: KnowledgePort) -> None:
        self._knowledge_port = knowledge_port

    def get_minimum_wall_thickness(self) -> OperationResult[float]:
        return OperationResult.ok(
            operation_id=str(uuid4()),
            data=self._knowledge_port.minimum_wall_thickness_mm(),
        )


---

## File originale: `implementation/python/src/spatial_intelligence/services/project_service.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/services/validation_service.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/services/workflow_service.py`

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


---

## File originale: `implementation/python/src/spatial_intelligence/validation/__init__.py`

"""Geometry and spatial validation rules."""

from .geometry_rules import (
    GeometryIssue,
    GeometryIssueCode,
    validate_opening_position,
    validate_perimeter,
    validate_wall_dimensions,
)

__all__ = [
    "GeometryIssue",
    "GeometryIssueCode",
    "validate_opening_position",
    "validate_perimeter",
    "validate_wall_dimensions",
]


---

## File originale: `implementation/python/src/spatial_intelligence/validation/geometry_rules.py`

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from spatial_intelligence.geometry import (
    Polyline2D,
    is_closed,
    segments_intersect,
)


class GeometryIssueCode(StrEnum):
    OPEN_PERIMETER = "OpenPerimeter"
    SELF_INTERSECTION = "SelfIntersection"
    INVALID_WALL_LENGTH = "InvalidWallLength"
    INVALID_WALL_THICKNESS = "InvalidWallThickness"
    INVALID_OPENING_WIDTH = "InvalidOpeningWidth"
    OPENING_OUTSIDE_HOST = "OpeningOutsideHost"


@dataclass(frozen=True, slots=True)
class GeometryIssue:
    code: GeometryIssueCode
    message: str
    subject_id: str | None = None


def validate_wall_dimensions(
    wall_id: str,
    length_mm: float,
    thickness_mm: float,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if length_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_WALL_LENGTH,
                message="Wall length must be greater than zero.",
                subject_id=wall_id,
            )
        )

    if thickness_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_WALL_THICKNESS,
                message="Wall thickness must be greater than zero.",
                subject_id=wall_id,
            )
        )

    return tuple(issues)


def validate_opening_position(
    opening_id: str,
    host_length_mm: float,
    offset_mm: float,
    width_mm: float,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if width_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_OPENING_WIDTH,
                message="Opening width must be greater than zero.",
                subject_id=opening_id,
            )
        )

    if (
        host_length_mm <= 0
        or offset_mm < 0
        or offset_mm + width_mm > host_length_mm
    ):
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.OPENING_OUTSIDE_HOST,
                message="Opening does not fit within its host element.",
                subject_id=opening_id,
            )
        )

    return tuple(issues)


def validate_perimeter(
    perimeter: Polyline2D,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if not is_closed(perimeter):
        return (
            GeometryIssue(
                code=GeometryIssueCode.OPEN_PERIMETER,
                message="The perimeter is not closed.",
            ),
        )

    segments = perimeter.segments
    segment_count = len(segments)

    for first_index, first in enumerate(segments):
        for second_index in range(first_index + 1, segment_count):
            second = segments[second_index]

            adjacent = (
                second_index == first_index + 1
                or (
                    first_index == 0
                    and second_index == segment_count - 1
                )
            )

            if adjacent:
                continue

            if segments_intersect(first, second):
                issues.append(
                    GeometryIssue(
                        code=GeometryIssueCode.SELF_INTERSECTION,
                        message=(
                            "The perimeter contains a "
                            "self-intersection."
                        ),
                    )
                )
                return tuple(issues)

    return tuple(issues)


---

## File originale: `implementation/python/tests/test_architecture_dependencies.py`

from pathlib import Path


SOURCE = (
    Path(__file__).parents[1]
    / "src"
    / "spatial_intelligence"
)


def read_module(relative_path: str) -> str:
    return (SOURCE / relative_path).read_text(encoding="utf-8")


def test_domain_does_not_import_services_or_adapters() -> None:
    content = read_module("domain/models.py")

    assert "spatial_intelligence.services" not in content
    assert "spatial_intelligence.adapters" not in content


def test_services_do_not_import_concrete_adapters() -> None:
    for path in (SOURCE / "services").glob("*.py"):
        content = path.read_text(encoding="utf-8")
        assert "spatial_intelligence.adapters" not in content


def test_ports_do_not_import_adapters() -> None:
    for path in (SOURCE / "ports").glob("*.py"):
        content = path.read_text(encoding="utf-8")
        assert "spatial_intelligence.adapters" not in content


---

## File originale: `implementation/python/tests/test_capability_registry.py`

from spatial_intelligence.capabilities import (
    Capability,
    CapabilityRegistry,
    build_default_registry,
)


def test_default_geometry_capabilities_are_available() -> None:
    registry = build_default_registry()

    assert registry.supports("geometry.polyline-2d")
    assert registry.supports("geometry.perimeter-validation")
    assert registry.supports("validation.opening-host")


def test_registry_returns_capabilities_in_stable_order() -> None:
    registry = CapabilityRegistry()

    registry.register(
        Capability("z-capability", "1.0", "Last")
    )
    registry.register(
        Capability("a-capability", "1.0", "First")
    )

    identifiers = tuple(
        capability.capability_id
        for capability in registry.list_all()
    )

    assert identifiers == (
        "a-capability",
        "z-capability",
    )


---

## File originale: `implementation/python/tests/test_events_and_plugins.py`

import pytest

from spatial_intelligence.events import Event, EventDispatcher
from spatial_intelligence.plugins import (
    PluginDescriptor,
    PluginRegistry,
)


def test_event_dispatcher_notifies_subscriber() -> None:
    dispatcher = EventDispatcher()
    received: list[str] = []

    dispatcher.subscribe(
        "ProjectSaved",
        lambda event: received.append(event.event_id),
    )

    event = Event.create(
        "ProjectSaved",
        {"projectId": "project_001"},
    )

    dispatcher.dispatch(event)

    assert received == [event.event_id]


def test_plugin_capability_discovery() -> None:
    registry = PluginRegistry()

    registry.register(
        PluginDescriptor(
            plugin_id="example.geojson",
            version="1.0.0",
            capabilities=("export.geojson",),
        )
    )

    assert registry.supports("export.geojson")


def test_duplicate_plugin_is_rejected() -> None:
    registry = PluginRegistry()
    descriptor = PluginDescriptor(
        plugin_id="duplicate",
        version="1.0.0",
        capabilities=(),
    )

    registry.register(descriptor)

    with pytest.raises(ValueError):
        registry.register(descriptor)


---

## File originale: `implementation/python/tests/test_geojson_interoperability.py`

import json

import pytest

from spatial_intelligence.domain import Project, Wall
from spatial_intelligence.interoperability import (
    GeoJsonError,
    export_project_geojson,
    import_walls_geojson,
)


def test_geojson_round_trip_for_walls() -> None:
    project = Project(
        project_id="project_geojson_001",
        name="GeoJSON Test",
        walls=(
            Wall(
                wall_id="wall_001",
                start=(0.0, 0.0),
                end=(4000.0, 0.0),
                thickness_mm=120.0,
            ),
        ),
    )

    payload = export_project_geojson(project)
    restored = import_walls_geojson(payload)

    assert restored == project.walls
    assert json.loads(payload)["type"] == "FeatureCollection"


def test_invalid_geojson_root_is_rejected() -> None:
    with pytest.raises(GeoJsonError):
        import_walls_geojson('{"type": "Point"}')


---

## File originale: `implementation/python/tests/test_geometry_algorithms.py`

import pytest

from spatial_intelligence.geometry import (
    Point2D,
    Polyline2D,
    Segment2D,
    closed_polyline_area,
    is_closed,
    polyline_length,
    segments_intersect,
    signed_area,
)


def test_closed_rectangle_area_and_length() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(4000.0, 0.0),
            Point2D(4000.0, 3000.0),
            Point2D(0.0, 3000.0),
            Point2D(0.0, 0.0),
        )
    )

    assert is_closed(perimeter)
    assert polyline_length(perimeter) == 14000.0
    assert closed_polyline_area(perimeter) == 12_000_000.0
    assert signed_area(perimeter) == 12_000_000.0


def test_open_polyline_has_no_area() -> None:
    polyline = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(1000.0, 0.0),
            Point2D(1000.0, 1000.0),
        )
    )

    assert not is_closed(polyline)

    with pytest.raises(ValueError):
        closed_polyline_area(polyline)


def test_crossing_segments_intersect() -> None:
    first = Segment2D(
        Point2D(0.0, 0.0),
        Point2D(1000.0, 1000.0),
    )
    second = Segment2D(
        Point2D(0.0, 1000.0),
        Point2D(1000.0, 0.0),
    )

    assert segments_intersect(first, second)


---

## File originale: `implementation/python/tests/test_geometry_service.py`

from spatial_intelligence.adapters import SimpleGeometryKernel
from spatial_intelligence.domain import Wall
from spatial_intelligence.services import GeometryService


def test_calculates_wall_length() -> None:
    service = GeometryService(SimpleGeometryKernel())

    wall = Wall(
        wall_id="wall_length_test",
        start=(0.0, 0.0),
        end=(3000.0, 4000.0),
        thickness_mm=120.0,
    )

    result = service.calculate_wall_length(wall)

    assert result.success is True
    assert result.data == 5000.0


---

## File originale: `implementation/python/tests/test_geometry_validation_rules.py`

from spatial_intelligence.geometry import Point2D, Polyline2D
from spatial_intelligence.validation import (
    GeometryIssueCode,
    validate_opening_position,
    validate_perimeter,
    validate_wall_dimensions,
)


def test_valid_rectangle_has_no_geometry_issues() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(4000.0, 0.0),
            Point2D(4000.0, 3000.0),
            Point2D(0.0, 3000.0),
            Point2D(0.0, 0.0),
        )
    )

    assert validate_perimeter(perimeter) == ()


def test_open_perimeter_is_rejected() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(1000.0, 0.0),
            Point2D(1000.0, 1000.0),
        )
    )

    issues = validate_perimeter(perimeter)

    assert issues[0].code == GeometryIssueCode.OPEN_PERIMETER


def test_self_intersection_is_rejected() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(2000.0, 2000.0),
            Point2D(0.0, 2000.0),
            Point2D(2000.0, 0.0),
            Point2D(0.0, 0.0),
        )
    )

    issues = validate_perimeter(perimeter)

    assert issues[0].code == GeometryIssueCode.SELF_INTERSECTION


def test_opening_outside_host_is_rejected() -> None:
    issues = validate_opening_position(
        opening_id="door_001",
        host_length_mm=3000.0,
        offset_mm=2500.0,
        width_mm=900.0,
    )

    assert (
        GeometryIssueCode.OPENING_OUTSIDE_HOST
        in {issue.code for issue in issues}
    )


def test_invalid_wall_dimensions_are_rejected() -> None:
    issues = validate_wall_dimensions(
        wall_id="wall_001",
        length_mm=0.0,
        thickness_mm=-10.0,
    )

    codes = {issue.code for issue in issues}

    assert GeometryIssueCode.INVALID_WALL_LENGTH in codes
    assert GeometryIssueCode.INVALID_WALL_THICKNESS in codes


---

## File originale: `implementation/python/tests/test_json_project_repository.py`

from pathlib import Path

from spatial_intelligence.adapters.json_project_repository import (
    JsonProjectRepository,
)
from spatial_intelligence.domain import Project, Wall
from spatial_intelligence.persistence import ProjectRecord


def test_json_repository_round_trip(tmp_path: Path) -> None:
    repository = JsonProjectRepository(tmp_path)

    project = Project(
        project_id="project_json_001",
        name="JSON Test",
        walls=(
            Wall(
                wall_id="wall_001",
                start=(0.0, 0.0),
                end=(4000.0, 0.0),
                thickness_mm=120.0,
            ),
        ),
    )

    stored = repository.save(ProjectRecord.initial(project))
    loaded = repository.load(project.project_id)

    assert loaded == stored
    assert repository.exists(project.project_id)


---

## File originale: `implementation/python/tests/test_project_service.py`

from spatial_intelligence.adapters.in_memory_project_repository import (
    InMemoryProjectRepository,
)
from spatial_intelligence.domain import Project
from spatial_intelligence.services.project_service import ProjectService


def test_save_and_load_project() -> None:
    service = ProjectService(InMemoryProjectRepository())

    project = Project(
        project_id="project_001",
        name="Persistence Test",
    )

    saved = service.save_project(project)
    loaded = service.load_project(project.project_id)

    assert saved.success is True
    assert saved.data is not None
    assert saved.data.revision == 1
    assert loaded.success is True
    assert loaded.data == saved.data


def test_revision_increases_after_update() -> None:
    service = ProjectService(InMemoryProjectRepository())

    original = Project(
        project_id="project_002",
        name="Original",
    )
    updated = Project(
        project_id="project_002",
        name="Updated",
    )

    first = service.save_project(original)
    second = service.save_project(
        updated,
        expected_revision=1,
    )

    assert first.data is not None
    assert second.data is not None
    assert second.data.revision == 2
    assert second.data.project.name == "Updated"


def test_revision_conflict_returns_failure() -> None:
    service = ProjectService(InMemoryProjectRepository())

    project = Project(
        project_id="project_003",
        name="Conflict Test",
    )

    service.save_project(project)

    result = service.save_project(
        project,
        expected_revision=99,
    )

    assert result.success is False
    assert result.errors[0].code.value == "RevisionConflict"


---

## File originale: `implementation/python/tests/test_public_api.py`

from spatial_intelligence.api import SpatialIntelligenceApp
from spatial_intelligence.config import RuntimeSettings


def test_stable_public_facade() -> None:
    app = SpatialIntelligenceApp(
        RuntimeSettings(environment="test")
    )

    assert app.health().status == "healthy"
    assert app.health().version == "1.0.0"
    assert len(app.capabilities()) >= 3
    assert app.services.workflow is not None


---

## File originale: `implementation/python/tests/test_reference_workflow.py`

from spatial_intelligence.composition import build_application
from spatial_intelligence.domain import Project, Wall


def test_validate_and_export_workflow() -> None:
    services = build_application()

    project = Project(
        project_id="project_test_001",
        name="Reference Test",
        walls=(
            Wall(
                wall_id="wall_001",
                start=(0.0, 0.0),
                end=(4000.0, 0.0),
                thickness_mm=120.0,
            ),
        ),
    )

    result = services.workflow.validate_and_export(project)

    assert result.success is True
    assert result.data is not None
    assert "project_test_001" in result.data
    assert len(result.event_ids) == 1
    assert services.event_bus.events[0]["eventType"] == "ExportCompleted"


---

## File originale: `implementation/python/tests/test_runtime_hardening.py`

from spatial_intelligence.config import RuntimeSettings
from spatial_intelligence.health import HealthService


def test_default_runtime_settings() -> None:
    settings = RuntimeSettings.from_environment()

    assert settings.environment
    assert settings.log_level


def test_health_service_reports_version() -> None:
    settings = RuntimeSettings(
        environment="test",
        log_level="WARNING",
        data_directory="./test-data",
    )

    status = HealthService(
        version="0.9.0",
        settings=settings,
    ).check()

    assert status.status == "healthy"
    assert status.version == "0.9.0"
    assert status.environment == "test"


---

## File originale: `implementation/python/tests/test_spatial_clearance.py`

from spatial_intelligence.analysis import (
    AxisAlignedBox,
    clearance_between,
    has_minimum_clearance,
)


def test_horizontal_clearance() -> None:
    first = AxisAlignedBox(0.0, 0.0, 1000.0, 1000.0)
    second = AxisAlignedBox(1800.0, 0.0, 2800.0, 1000.0)

    assert clearance_between(first, second) == 800.0
    assert has_minimum_clearance(first, second, 800.0)


def test_overlapping_boxes_have_zero_clearance() -> None:
    first = AxisAlignedBox(0.0, 0.0, 1000.0, 1000.0)
    second = AxisAlignedBox(500.0, 500.0, 1500.0, 1500.0)

    assert clearance_between(first, second) == 0.0
    assert not has_minimum_clearance(
        first,
        second,
        1.0,
    )


---

## File originale: `implementation/python/tests/test_validation_service.py`

from spatial_intelligence.adapters import StaticKnowledgeAdapter
from spatial_intelligence.domain import Project, Wall
from spatial_intelligence.services import ValidationService


def test_rejects_wall_below_minimum_thickness() -> None:
    service = ValidationService(
        StaticKnowledgeAdapter(minimum_thickness_mm=100.0)
    )

    project = Project(
        project_id="project_invalid_001",
        name="Invalid Project",
        walls=(
            Wall(
                wall_id="wall_too_thin",
                start=(0.0, 0.0),
                end=(1000.0, 0.0),
                thickness_mm=80.0,
            ),
        ),
    )

    result = service.validate_project(project)

    assert result.success is False
    assert result.errors[0].subject_id == "wall_too_thin"


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

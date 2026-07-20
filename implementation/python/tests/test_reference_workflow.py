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

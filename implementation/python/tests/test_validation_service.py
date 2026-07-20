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

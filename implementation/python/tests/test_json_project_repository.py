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

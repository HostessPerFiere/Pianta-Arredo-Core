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

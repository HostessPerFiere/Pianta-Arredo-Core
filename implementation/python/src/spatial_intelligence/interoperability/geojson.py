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

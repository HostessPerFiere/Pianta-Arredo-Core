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

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

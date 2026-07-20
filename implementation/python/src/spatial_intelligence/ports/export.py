from __future__ import annotations

from typing import Protocol

from spatial_intelligence.domain import Project


class ExportPort(Protocol):
    def export_project(self, project: Project) -> str:
        """Return a serialised export artifact."""
        ...

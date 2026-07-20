from __future__ import annotations

from typing import Protocol


class KnowledgePort(Protocol):
    def minimum_wall_thickness_mm(self) -> float:
        """Return the configured minimum Wall thickness."""
        ...

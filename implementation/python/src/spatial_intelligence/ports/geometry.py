from __future__ import annotations

from typing import Protocol

from spatial_intelligence.domain import Wall


class GeometryPort(Protocol):
    def wall_length_mm(self, wall: Wall) -> float:
        """Return Wall length in millimetres."""
        ...

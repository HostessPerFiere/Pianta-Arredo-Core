from __future__ import annotations

from math import hypot

from spatial_intelligence.domain import Wall


class SimpleGeometryKernel:
    def wall_length_mm(self, wall: Wall) -> float:
        return hypot(
            wall.end[0] - wall.start[0],
            wall.end[1] - wall.start[1],
        )

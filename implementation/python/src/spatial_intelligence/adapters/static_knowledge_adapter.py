from __future__ import annotations


class StaticKnowledgeAdapter:
    def __init__(self, minimum_thickness_mm: float = 80.0) -> None:
        if minimum_thickness_mm <= 0:
            raise ValueError("minimum_thickness_mm must be positive")

        self._minimum_thickness_mm = minimum_thickness_mm

    def minimum_wall_thickness_mm(self) -> float:
        return self._minimum_thickness_mm

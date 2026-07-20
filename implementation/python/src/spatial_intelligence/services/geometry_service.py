from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.domain import Wall
from spatial_intelligence.ports import GeometryPort


class GeometryService:
    def __init__(self, geometry_port: GeometryPort) -> None:
        self._geometry_port = geometry_port

    def calculate_wall_length(
        self,
        wall: Wall,
    ) -> OperationResult[float]:
        operation_id = str(uuid4())
        length = self._geometry_port.wall_length_mm(wall)

        return OperationResult.ok(
            operation_id=operation_id,
            data=length,
        )

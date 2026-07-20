from __future__ import annotations

from uuid import uuid4

from spatial_intelligence.contracts import OperationResult
from spatial_intelligence.ports import KnowledgePort


class KnowledgeService:
    def __init__(self, knowledge_port: KnowledgePort) -> None:
        self._knowledge_port = knowledge_port

    def get_minimum_wall_thickness(self) -> OperationResult[float]:
        return OperationResult.ok(
            operation_id=str(uuid4()),
            data=self._knowledge_port.minimum_wall_thickness_mm(),
        )

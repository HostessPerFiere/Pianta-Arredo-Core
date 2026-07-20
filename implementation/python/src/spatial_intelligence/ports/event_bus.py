from __future__ import annotations

from typing import Mapping, Protocol


class EventBusPort(Protocol):
    def publish(self, event_type: str, payload: Mapping[str, object]) -> str:
        """Publish an Event and return its identifier."""
        ...

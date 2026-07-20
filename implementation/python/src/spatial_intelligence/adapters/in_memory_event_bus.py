from __future__ import annotations

from collections.abc import Mapping
from uuid import uuid4


class InMemoryEventBus:
    def __init__(self) -> None:
        self.events: list[dict[str, object]] = []

    def publish(
        self,
        event_type: str,
        payload: Mapping[str, object],
    ) -> str:
        event_id = str(uuid4())

        self.events.append(
            {
                "eventId": event_id,
                "eventType": event_type,
                "payload": dict(payload),
            }
        )

        return event_id

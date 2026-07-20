from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    event_type: str
    payload: Mapping[str, object]

    @classmethod
    def create(
        cls,
        event_type: str,
        payload: Mapping[str, object],
    ) -> "Event":
        if not event_type:
            raise ValueError(
                "event_type must not be empty"
            )

        return cls(
            event_id=str(uuid4()),
            event_type=event_type,
            payload=dict(payload),
        )


EventHandler = Callable[[Event], None]


class EventDispatcher:
    def __init__(self) -> None:
        self._handlers: dict[
            str,
            list[EventHandler],
        ] = {}

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        self._handlers.setdefault(
            event_type,
            [],
        ).append(handler)

    def dispatch(self, event: Event) -> None:
        for handler in self._handlers.get(
            event.event_type,
            [],
        ):
            handler(event)

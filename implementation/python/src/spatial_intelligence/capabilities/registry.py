from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Capability:
    capability_id: str
    version: str
    description: str


class CapabilityRegistry:
    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        existing = self._capabilities.get(
            capability.capability_id
        )

        if existing is not None and existing != capability:
            raise ValueError(
                "Capability already registered with "
                "different metadata"
            )

        self._capabilities[
            capability.capability_id
        ] = capability

    def supports(self, capability_id: str) -> bool:
        return capability_id in self._capabilities

    def get(self, capability_id: str) -> Capability | None:
        return self._capabilities.get(capability_id)

    def list_all(self) -> tuple[Capability, ...]:
        return tuple(
            sorted(
                self._capabilities.values(),
                key=lambda capability: capability.capability_id,
            )
        )


def build_default_registry() -> CapabilityRegistry:
    registry = CapabilityRegistry()

    registry.register(
        Capability(
            capability_id="geometry.polyline-2d",
            version="0.4",
            description=(
                "Two-dimensional Point, Segment and Polyline support."
            ),
        )
    )

    registry.register(
        Capability(
            capability_id="geometry.perimeter-validation",
            version="0.4",
            description=(
                "Closed-perimeter and self-intersection validation."
            ),
        )
    )

    registry.register(
        Capability(
            capability_id="validation.opening-host",
            version="0.4",
            description=(
                "Opening placement validation against host length."
            ),
        )
    )

    return registry

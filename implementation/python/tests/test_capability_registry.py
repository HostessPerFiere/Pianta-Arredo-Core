from spatial_intelligence.capabilities import (
    Capability,
    CapabilityRegistry,
    build_default_registry,
)


def test_default_geometry_capabilities_are_available() -> None:
    registry = build_default_registry()

    assert registry.supports("geometry.polyline-2d")
    assert registry.supports("geometry.perimeter-validation")
    assert registry.supports("validation.opening-host")


def test_registry_returns_capabilities_in_stable_order() -> None:
    registry = CapabilityRegistry()

    registry.register(
        Capability("z-capability", "1.0", "Last")
    )
    registry.register(
        Capability("a-capability", "1.0", "First")
    )

    identifiers = tuple(
        capability.capability_id
        for capability in registry.list_all()
    )

    assert identifiers == (
        "a-capability",
        "z-capability",
    )

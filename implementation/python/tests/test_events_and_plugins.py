import pytest

from spatial_intelligence.events import Event, EventDispatcher
from spatial_intelligence.plugins import (
    PluginDescriptor,
    PluginRegistry,
)


def test_event_dispatcher_notifies_subscriber() -> None:
    dispatcher = EventDispatcher()
    received: list[str] = []

    dispatcher.subscribe(
        "ProjectSaved",
        lambda event: received.append(event.event_id),
    )

    event = Event.create(
        "ProjectSaved",
        {"projectId": "project_001"},
    )

    dispatcher.dispatch(event)

    assert received == [event.event_id]


def test_plugin_capability_discovery() -> None:
    registry = PluginRegistry()

    registry.register(
        PluginDescriptor(
            plugin_id="example.geojson",
            version="1.0.0",
            capabilities=("export.geojson",),
        )
    )

    assert registry.supports("export.geojson")


def test_duplicate_plugin_is_rejected() -> None:
    registry = PluginRegistry()
    descriptor = PluginDescriptor(
        plugin_id="duplicate",
        version="1.0.0",
        capabilities=(),
    )

    registry.register(descriptor)

    with pytest.raises(ValueError):
        registry.register(descriptor)

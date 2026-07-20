from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PluginDescriptor:
    plugin_id: str
    version: str
    capabilities: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.plugin_id:
            raise ValueError(
                "plugin_id must not be empty"
            )


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[
            str,
            PluginDescriptor,
        ] = {}

    def register(
        self,
        descriptor: PluginDescriptor,
    ) -> None:
        if descriptor.plugin_id in self._plugins:
            raise ValueError(
                "Plugin is already registered"
            )

        self._plugins[
            descriptor.plugin_id
        ] = descriptor

    def get(
        self,
        plugin_id: str,
    ) -> PluginDescriptor | None:
        return self._plugins.get(plugin_id)

    def supports(
        self,
        capability_id: str,
    ) -> bool:
        return any(
            capability_id in plugin.capabilities
            for plugin in self._plugins.values()
        )

    def list_all(
        self,
    ) -> tuple[PluginDescriptor, ...]:
        return tuple(
            sorted(
                self._plugins.values(),
                key=lambda plugin: plugin.plugin_id,
            )
        )

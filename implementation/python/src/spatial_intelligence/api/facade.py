from __future__ import annotations

from spatial_intelligence.capabilities import (
    Capability,
    build_default_registry,
)
from spatial_intelligence.composition import (
    ApplicationServices,
    build_application,
)
from spatial_intelligence.config import RuntimeSettings
from spatial_intelligence.health import (
    HealthService,
    HealthStatus,
)


class SpatialIntelligenceApp:
    def __init__(
        self,
        settings: RuntimeSettings | None = None,
    ) -> None:
        self._settings = (
            settings
            if settings is not None
            else RuntimeSettings.from_environment()
        )
        self._services = build_application()
        self._capabilities = build_default_registry()
        self._health = HealthService(
            version="1.0.0",
            settings=self._settings,
        )

    @property
    def services(self) -> ApplicationServices:
        return self._services

    def health(self) -> HealthStatus:
        return self._health.check()

    def capabilities(self) -> tuple[Capability, ...]:
        return self._capabilities.list_all()

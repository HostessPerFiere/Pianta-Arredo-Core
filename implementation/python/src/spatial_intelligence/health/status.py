from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from spatial_intelligence.config import RuntimeSettings


@dataclass(frozen=True, slots=True)
class HealthStatus:
    status: str
    version: str
    environment: str
    checked_at: str


class HealthService:
    def __init__(
        self,
        version: str,
        settings: RuntimeSettings,
    ) -> None:
        self._version = version
        self._settings = settings

    def check(self) -> HealthStatus:
        return HealthStatus(
            status="healthy",
            version=self._version,
            environment=self._settings.environment,
            checked_at=datetime.now(UTC).isoformat(),
        )

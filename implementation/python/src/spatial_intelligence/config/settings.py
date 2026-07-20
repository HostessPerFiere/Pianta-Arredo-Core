from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeSettings:
    environment: str = "development"
    log_level: str = "INFO"
    data_directory: str = "./data"

    @classmethod
    def from_environment(cls) -> "RuntimeSettings":
        return cls(
            environment=os.getenv(
                "SPATIAL_ENVIRONMENT",
                "development",
            ),
            log_level=os.getenv(
                "SPATIAL_LOG_LEVEL",
                "INFO",
            ).upper(),
            data_directory=os.getenv(
                "SPATIAL_DATA_DIRECTORY",
                "./data",
            ),
        )

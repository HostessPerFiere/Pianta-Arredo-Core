from spatial_intelligence.config import RuntimeSettings
from spatial_intelligence.health import HealthService


def test_default_runtime_settings() -> None:
    settings = RuntimeSettings.from_environment()

    assert settings.environment
    assert settings.log_level


def test_health_service_reports_version() -> None:
    settings = RuntimeSettings(
        environment="test",
        log_level="WARNING",
        data_directory="./test-data",
    )

    status = HealthService(
        version="0.9.0",
        settings=settings,
    ).check()

    assert status.status == "healthy"
    assert status.version == "0.9.0"
    assert status.environment == "test"

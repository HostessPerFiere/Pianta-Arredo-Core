from spatial_intelligence.api import SpatialIntelligenceApp
from spatial_intelligence.config import RuntimeSettings


def test_stable_public_facade() -> None:
    app = SpatialIntelligenceApp(
        RuntimeSettings(environment="test")
    )

    assert app.health().status == "healthy"
    assert app.health().version == "1.0.0"
    assert len(app.capabilities()) >= 3
    assert app.services.workflow is not None

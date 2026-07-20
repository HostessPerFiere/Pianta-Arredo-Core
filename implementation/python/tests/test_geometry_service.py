from spatial_intelligence.adapters import SimpleGeometryKernel
from spatial_intelligence.domain import Wall
from spatial_intelligence.services import GeometryService


def test_calculates_wall_length() -> None:
    service = GeometryService(SimpleGeometryKernel())

    wall = Wall(
        wall_id="wall_length_test",
        start=(0.0, 0.0),
        end=(3000.0, 4000.0),
        thickness_mm=120.0,
    )

    result = service.calculate_wall_length(wall)

    assert result.success is True
    assert result.data == 5000.0

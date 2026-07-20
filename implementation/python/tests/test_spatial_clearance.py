from spatial_intelligence.analysis import (
    AxisAlignedBox,
    clearance_between,
    has_minimum_clearance,
)


def test_horizontal_clearance() -> None:
    first = AxisAlignedBox(0.0, 0.0, 1000.0, 1000.0)
    second = AxisAlignedBox(1800.0, 0.0, 2800.0, 1000.0)

    assert clearance_between(first, second) == 800.0
    assert has_minimum_clearance(first, second, 800.0)


def test_overlapping_boxes_have_zero_clearance() -> None:
    first = AxisAlignedBox(0.0, 0.0, 1000.0, 1000.0)
    second = AxisAlignedBox(500.0, 500.0, 1500.0, 1500.0)

    assert clearance_between(first, second) == 0.0
    assert not has_minimum_clearance(
        first,
        second,
        1.0,
    )

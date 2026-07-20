import pytest

from spatial_intelligence.geometry import (
    Point2D,
    Polyline2D,
    Segment2D,
    closed_polyline_area,
    is_closed,
    polyline_length,
    segments_intersect,
    signed_area,
)


def test_closed_rectangle_area_and_length() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(4000.0, 0.0),
            Point2D(4000.0, 3000.0),
            Point2D(0.0, 3000.0),
            Point2D(0.0, 0.0),
        )
    )

    assert is_closed(perimeter)
    assert polyline_length(perimeter) == 14000.0
    assert closed_polyline_area(perimeter) == 12_000_000.0
    assert signed_area(perimeter) == 12_000_000.0


def test_open_polyline_has_no_area() -> None:
    polyline = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(1000.0, 0.0),
            Point2D(1000.0, 1000.0),
        )
    )

    assert not is_closed(polyline)

    with pytest.raises(ValueError):
        closed_polyline_area(polyline)


def test_crossing_segments_intersect() -> None:
    first = Segment2D(
        Point2D(0.0, 0.0),
        Point2D(1000.0, 1000.0),
    )
    second = Segment2D(
        Point2D(0.0, 1000.0),
        Point2D(1000.0, 0.0),
    )

    assert segments_intersect(first, second)

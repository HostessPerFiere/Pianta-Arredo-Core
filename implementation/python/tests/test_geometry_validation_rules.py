from spatial_intelligence.geometry import Point2D, Polyline2D
from spatial_intelligence.validation import (
    GeometryIssueCode,
    validate_opening_position,
    validate_perimeter,
    validate_wall_dimensions,
)


def test_valid_rectangle_has_no_geometry_issues() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(4000.0, 0.0),
            Point2D(4000.0, 3000.0),
            Point2D(0.0, 3000.0),
            Point2D(0.0, 0.0),
        )
    )

    assert validate_perimeter(perimeter) == ()


def test_open_perimeter_is_rejected() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(1000.0, 0.0),
            Point2D(1000.0, 1000.0),
        )
    )

    issues = validate_perimeter(perimeter)

    assert issues[0].code == GeometryIssueCode.OPEN_PERIMETER


def test_self_intersection_is_rejected() -> None:
    perimeter = Polyline2D(
        (
            Point2D(0.0, 0.0),
            Point2D(2000.0, 2000.0),
            Point2D(0.0, 2000.0),
            Point2D(2000.0, 0.0),
            Point2D(0.0, 0.0),
        )
    )

    issues = validate_perimeter(perimeter)

    assert issues[0].code == GeometryIssueCode.SELF_INTERSECTION


def test_opening_outside_host_is_rejected() -> None:
    issues = validate_opening_position(
        opening_id="door_001",
        host_length_mm=3000.0,
        offset_mm=2500.0,
        width_mm=900.0,
    )

    assert (
        GeometryIssueCode.OPENING_OUTSIDE_HOST
        in {issue.code for issue in issues}
    )


def test_invalid_wall_dimensions_are_rejected() -> None:
    issues = validate_wall_dimensions(
        wall_id="wall_001",
        length_mm=0.0,
        thickness_mm=-10.0,
    )

    codes = {issue.code for issue in issues}

    assert GeometryIssueCode.INVALID_WALL_LENGTH in codes
    assert GeometryIssueCode.INVALID_WALL_THICKNESS in codes

from __future__ import annotations

from math import isclose

from .primitives import Point2D, Polyline2D, Segment2D


def polyline_length(polyline: Polyline2D) -> float:
    return sum(segment.length for segment in polyline.segments)


def is_closed(
    polyline: Polyline2D,
    tolerance: float = 1e-9,
) -> bool:
    first = polyline.points[0]
    last = polyline.points[-1]

    return (
        isclose(first.x, last.x, abs_tol=tolerance)
        and isclose(first.y, last.y, abs_tol=tolerance)
    )


def signed_area(polyline: Polyline2D) -> float:
    if not is_closed(polyline):
        raise ValueError("Area requires a closed Polyline2D")

    total = 0.0

    for current, following in zip(
        polyline.points,
        polyline.points[1:],
    ):
        total += (
            current.x * following.y
            - following.x * current.y
        )

    return total / 2.0


def closed_polyline_area(polyline: Polyline2D) -> float:
    return abs(signed_area(polyline))


def _orientation(
    first: Point2D,
    second: Point2D,
    third: Point2D,
    tolerance: float,
) -> int:
    value = (
        (second.y - first.y) * (third.x - second.x)
        - (second.x - first.x) * (third.y - second.y)
    )

    if isclose(value, 0.0, abs_tol=tolerance):
        return 0

    return 1 if value > 0 else 2


def _on_segment(
    first: Point2D,
    point: Point2D,
    second: Point2D,
    tolerance: float,
) -> bool:
    return (
        min(first.x, second.x) - tolerance
        <= point.x
        <= max(first.x, second.x) + tolerance
        and min(first.y, second.y) - tolerance
        <= point.y
        <= max(first.y, second.y) + tolerance
    )


def segments_intersect(
    first: Segment2D,
    second: Segment2D,
    tolerance: float = 1e-9,
) -> bool:
    p1 = first.start
    q1 = first.end
    p2 = second.start
    q2 = second.end

    o1 = _orientation(p1, q1, p2, tolerance)
    o2 = _orientation(p1, q1, q2, tolerance)
    o3 = _orientation(p2, q2, p1, tolerance)
    o4 = _orientation(p2, q2, q1, tolerance)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and _on_segment(p1, p2, q1, tolerance):
        return True

    if o2 == 0 and _on_segment(p1, q2, q1, tolerance):
        return True

    if o3 == 0 and _on_segment(p2, p1, q2, tolerance):
        return True

    if o4 == 0 and _on_segment(p2, q1, q2, tolerance):
        return True

    return False

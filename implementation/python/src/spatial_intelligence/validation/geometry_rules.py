from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from spatial_intelligence.geometry import (
    Polyline2D,
    is_closed,
    segments_intersect,
)


class GeometryIssueCode(StrEnum):
    OPEN_PERIMETER = "OpenPerimeter"
    SELF_INTERSECTION = "SelfIntersection"
    INVALID_WALL_LENGTH = "InvalidWallLength"
    INVALID_WALL_THICKNESS = "InvalidWallThickness"
    INVALID_OPENING_WIDTH = "InvalidOpeningWidth"
    OPENING_OUTSIDE_HOST = "OpeningOutsideHost"


@dataclass(frozen=True, slots=True)
class GeometryIssue:
    code: GeometryIssueCode
    message: str
    subject_id: str | None = None


def validate_wall_dimensions(
    wall_id: str,
    length_mm: float,
    thickness_mm: float,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if length_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_WALL_LENGTH,
                message="Wall length must be greater than zero.",
                subject_id=wall_id,
            )
        )

    if thickness_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_WALL_THICKNESS,
                message="Wall thickness must be greater than zero.",
                subject_id=wall_id,
            )
        )

    return tuple(issues)


def validate_opening_position(
    opening_id: str,
    host_length_mm: float,
    offset_mm: float,
    width_mm: float,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if width_mm <= 0:
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.INVALID_OPENING_WIDTH,
                message="Opening width must be greater than zero.",
                subject_id=opening_id,
            )
        )

    if (
        host_length_mm <= 0
        or offset_mm < 0
        or offset_mm + width_mm > host_length_mm
    ):
        issues.append(
            GeometryIssue(
                code=GeometryIssueCode.OPENING_OUTSIDE_HOST,
                message="Opening does not fit within its host element.",
                subject_id=opening_id,
            )
        )

    return tuple(issues)


def validate_perimeter(
    perimeter: Polyline2D,
) -> tuple[GeometryIssue, ...]:
    issues: list[GeometryIssue] = []

    if not is_closed(perimeter):
        return (
            GeometryIssue(
                code=GeometryIssueCode.OPEN_PERIMETER,
                message="The perimeter is not closed.",
            ),
        )

    segments = perimeter.segments
    segment_count = len(segments)

    for first_index, first in enumerate(segments):
        for second_index in range(first_index + 1, segment_count):
            second = segments[second_index]

            adjacent = (
                second_index == first_index + 1
                or (
                    first_index == 0
                    and second_index == segment_count - 1
                )
            )

            if adjacent:
                continue

            if segments_intersect(first, second):
                issues.append(
                    GeometryIssue(
                        code=GeometryIssueCode.SELF_INTERSECTION,
                        message=(
                            "The perimeter contains a "
                            "self-intersection."
                        ),
                    )
                )
                return tuple(issues)

    return tuple(issues)

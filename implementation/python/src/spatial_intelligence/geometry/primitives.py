from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True, slots=True)
class Point2D:
    x: float
    y: float

    def distance_to(self, other: "Point2D") -> float:
        return hypot(other.x - self.x, other.y - self.y)


@dataclass(frozen=True, slots=True)
class Segment2D:
    start: Point2D
    end: Point2D

    def __post_init__(self) -> None:
        if self.start == self.end:
            raise ValueError("A Segment2D requires two different points")

    @property
    def length(self) -> float:
        return self.start.distance_to(self.end)


@dataclass(frozen=True, slots=True)
class Polyline2D:
    points: tuple[Point2D, ...]

    def __post_init__(self) -> None:
        if len(self.points) < 2:
            raise ValueError("A Polyline2D requires at least two points")

    @property
    def segments(self) -> tuple[Segment2D, ...]:
        return tuple(
            Segment2D(start, end)
            for start, end in zip(self.points, self.points[1:])
        )

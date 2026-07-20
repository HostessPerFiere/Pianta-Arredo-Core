"""Technology-neutral two-dimensional geometry utilities."""

from .algorithms import (
    closed_polyline_area,
    is_closed,
    polyline_length,
    segments_intersect,
    signed_area,
)
from .primitives import Point2D, Polyline2D, Segment2D

__all__ = [
    "Point2D",
    "Polyline2D",
    "Segment2D",
    "closed_polyline_area",
    "is_closed",
    "polyline_length",
    "segments_intersect",
    "signed_area",
]

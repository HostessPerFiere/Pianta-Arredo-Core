"""Geometry and spatial validation rules."""

from .geometry_rules import (
    GeometryIssue,
    GeometryIssueCode,
    validate_opening_position,
    validate_perimeter,
    validate_wall_dimensions,
)

__all__ = [
    "GeometryIssue",
    "GeometryIssueCode",
    "validate_opening_position",
    "validate_perimeter",
    "validate_wall_dimensions",
]

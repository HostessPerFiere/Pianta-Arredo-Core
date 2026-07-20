"""Deterministic spatial analysis utilities."""

from .clearance import (
    AxisAlignedBox,
    clearance_between,
    has_minimum_clearance,
)

__all__ = [
    "AxisAlignedBox",
    "clearance_between",
    "has_minimum_clearance",
]

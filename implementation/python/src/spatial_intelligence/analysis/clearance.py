from __future__ import annotations

from dataclasses import dataclass
from math import hypot


@dataclass(frozen=True, slots=True)
class AxisAlignedBox:
    minimum_x: float
    minimum_y: float
    maximum_x: float
    maximum_y: float

    def __post_init__(self) -> None:
        if self.maximum_x <= self.minimum_x:
            raise ValueError(
                "maximum_x must exceed minimum_x"
            )

        if self.maximum_y <= self.minimum_y:
            raise ValueError(
                "maximum_y must exceed minimum_y"
            )


def clearance_between(
    first: AxisAlignedBox,
    second: AxisAlignedBox,
) -> float:
    horizontal = max(
        first.minimum_x - second.maximum_x,
        second.minimum_x - first.maximum_x,
        0.0,
    )

    vertical = max(
        first.minimum_y - second.maximum_y,
        second.minimum_y - first.maximum_y,
        0.0,
    )

    return hypot(horizontal, vertical)


def has_minimum_clearance(
    first: AxisAlignedBox,
    second: AxisAlignedBox,
    minimum_clearance: float,
) -> bool:
    if minimum_clearance < 0:
        raise ValueError(
            "minimum_clearance must not be negative"
        )

    return (
        clearance_between(first, second)
        >= minimum_clearance
    )

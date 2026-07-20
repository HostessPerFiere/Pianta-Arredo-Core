from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

from .errors import ServiceError

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class OperationResult(Generic[T]):
    operation_id: str
    success: bool
    data: T | None = None
    errors: tuple[ServiceError, ...] = field(default_factory=tuple)
    warnings: tuple[ServiceError, ...] = field(default_factory=tuple)
    event_ids: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def ok(
        cls,
        operation_id: str,
        data: T,
        event_ids: tuple[str, ...] = (),
    ) -> "OperationResult[T]":
        return cls(
            operation_id=operation_id,
            success=True,
            data=data,
            event_ids=event_ids,
        )

    @classmethod
    def fail(
        cls,
        operation_id: str,
        *errors: ServiceError,
    ) -> "OperationResult[T]":
        return cls(
            operation_id=operation_id,
            success=False,
            errors=tuple(errors),
        )

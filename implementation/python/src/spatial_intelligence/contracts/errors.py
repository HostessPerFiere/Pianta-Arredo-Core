from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class ErrorCode(StrEnum):
    INVALID_REQUEST = "InvalidRequest"
    ENTITY_NOT_FOUND = "EntityNotFound"
    VALIDATION_FAILED = "ValidationFailed"
    REVISION_CONFLICT = "RevisionConflict"
    CAPABILITY_NOT_SUPPORTED = "CapabilityNotSupported"
    INTERNAL_FAILURE = "InternalFailure"


@dataclass(frozen=True, slots=True)
class ServiceError:
    code: ErrorCode
    message: str
    recoverable: bool
    subject_id: str | None = None
    suggested_action: str | None = None

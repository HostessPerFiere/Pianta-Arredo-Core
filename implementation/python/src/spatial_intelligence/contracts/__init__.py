"""Public request, result and error contracts."""

from .errors import ErrorCode, ServiceError
from .results import OperationResult

__all__ = ["ErrorCode", "OperationResult", "ServiceError"]

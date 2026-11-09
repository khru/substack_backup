from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

import pybreaker

from substack_sync.circuit_breaker_open_error import CircuitBreakerOpenError

ResultType = TypeVar("ResultType")


class PyBreakerCircuitBreaker:
    def __init__(self, fail_max: int, reset_timeout_seconds: int) -> None:
        self._breaker = pybreaker.CircuitBreaker(
            fail_max=fail_max,
            reset_timeout=reset_timeout_seconds,
        )

    def call(self, operation: Callable[[], ResultType]) -> ResultType:
        try:
            return self._breaker.call(operation)
        except pybreaker.CircuitBreakerError as error:
            raise CircuitBreakerOpenError("Circuit breaker is open.") from error

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, TypeVar

import pybreaker
from urllib3.util.retry import Retry

from substack_sync.errors import CircuitBreakerOpenError

_RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

_ResultType = TypeVar("_ResultType")


class CircuitBreakerPort(Protocol):
    def call(self, operation: Callable[[], _ResultType]) -> _ResultType: ...


class NullCircuitBreaker:
    def call(self, operation: Callable[[], _ResultType]) -> _ResultType:
        return operation()


class PyBreakerCircuitBreaker:
    def __init__(self, fail_max: int, reset_timeout_seconds: int) -> None:
        self._breaker = pybreaker.CircuitBreaker(
            fail_max=fail_max,
            reset_timeout=reset_timeout_seconds,
        )

    def call(self, operation: Callable[[], _ResultType]) -> _ResultType:
        try:
            return self._breaker.call(operation)
        except pybreaker.CircuitBreakerError as error:
            raise CircuitBreakerOpenError("Circuit breaker is open.") from error


def build_retry_policy(max_retries: int) -> Retry:
    return Retry(
        total=max_retries,
        connect=max_retries,
        read=max_retries,
        status=max_retries,
        backoff_factor=0.5,
        status_forcelist=_RETRYABLE_STATUS_CODES,
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )


def build_circuit_breaker(fail_max: int, reset_timeout_seconds: int) -> CircuitBreakerPort:
    return PyBreakerCircuitBreaker(
        fail_max=fail_max,
        reset_timeout_seconds=reset_timeout_seconds,
    )

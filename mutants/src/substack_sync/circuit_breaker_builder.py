from __future__ import annotations

from substack_sync.circuit_breaker_port import CircuitBreakerPort
from substack_sync.pybreaker_circuit_breaker import PyBreakerCircuitBreaker


def build_circuit_breaker(fail_max: int, reset_timeout_seconds: int) -> CircuitBreakerPort:
    return PyBreakerCircuitBreaker(
        fail_max=fail_max,
        reset_timeout_seconds=reset_timeout_seconds,
    )

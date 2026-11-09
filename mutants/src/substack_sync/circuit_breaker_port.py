from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, TypeVar

ResultType = TypeVar("ResultType")


class CircuitBreakerPort(Protocol):
    def call(self, operation: Callable[[], ResultType]) -> ResultType: ...

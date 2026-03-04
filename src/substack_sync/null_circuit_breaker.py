from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

ResultType = TypeVar("ResultType")


class NullCircuitBreaker:
    def call(self, operation: Callable[[], ResultType]) -> ResultType:
        return operation()

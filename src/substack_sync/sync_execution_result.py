from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SyncExecutionResult:
    downloaded: int
    failed: int
    failures: tuple[str, ...]

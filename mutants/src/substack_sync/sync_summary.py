from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SyncSummary:
    total_urls: int
    downloaded: int
    skipped_existing: int
    failed: int
    failures: tuple[str, ...]

    @property
    def has_failures(self) -> bool:
        return self.failed > 0

    def to_log_lines(self) -> tuple[str, ...]:
        return (
            f"Total feed URLs: {self.total_urls}",
            f"Downloaded posts: {self.downloaded}",
            f"Skipped existing posts: {self.skipped_existing}",
            f"Failed downloads: {self.failed}",
        )

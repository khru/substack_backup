from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ImageBackupSummary:
    total_posts: int
    images_discovered: int
    downloaded: int
    skipped_existing: int
    failed: int
    failures: tuple[str, ...]

    @property
    def has_failures(self) -> bool:
        return self.failed > 0

    def to_log_lines(self) -> tuple[str, ...]:
        return (
            f"Total markdown posts: {self.total_posts}",
            f"Discovered images: {self.images_discovered}",
            f"Downloaded images: {self.downloaded}",
            f"Skipped existing images: {self.skipped_existing}",
            f"Failed downloads: {self.failed}",
        )

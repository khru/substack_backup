from __future__ import annotations

from typing import Protocol

from substack_sync.archive_parser import ArchivePost


class ArchiveReader(Protocol):
    def fetch(self, archive_url: str) -> tuple[ArchivePost, ...]:
        """Return archive posts including canonical URLs and publication timestamps."""
        ...

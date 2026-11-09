from __future__ import annotations

from dataclasses import dataclass

from substack_sync.download_candidate import DownloadCandidate


@dataclass(frozen=True)
class SyncPlan:
    download_candidates: tuple[DownloadCandidate, ...]
    skipped_existing: int
    rejected_urls: tuple[str, ...]

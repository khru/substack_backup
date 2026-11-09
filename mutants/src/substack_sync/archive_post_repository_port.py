from __future__ import annotations

from typing import Protocol

from substack_sync.models import MarkdownDocument, Slug


class ArchivePostRepository(Protocol):
    def upsert_post(self, slug: Slug, published_timestamp: str, document: MarkdownDocument) -> bool:
        """Persist or update timestamped markdown. Return True when filesystem changed."""
        ...

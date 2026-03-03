from __future__ import annotations

from pathlib import Path
from typing import Protocol

from substack_sync.models import MarkdownDocument, Slug


class FeedReader(Protocol):
    def fetch(self, feed_url: str) -> str:
        """Return raw RSS/Atom XML text for a feed URL."""
        ...


class MarkdownFetcher(Protocol):
    def fetch(self, article_url: str) -> str:
        """Return markdown text for an article URL."""
        ...


class PostRepository(Protocol):
    def existing_slug_values(self) -> frozenset[str]:
        """Return existing slug values already persisted."""
        ...

    def save_post(self, slug: Slug, document: MarkdownDocument) -> Path:
        """Persist markdown and return saved path."""
        ...

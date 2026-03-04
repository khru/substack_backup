from __future__ import annotations

from typing import Protocol


class MarkdownFetcher(Protocol):
    def fetch(self, article_url: str) -> str:
        """Return markdown text for an article URL."""
        ...

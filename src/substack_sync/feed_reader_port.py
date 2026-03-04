from __future__ import annotations

from typing import Protocol


class FeedReader(Protocol):
    def fetch(self, feed_url: str) -> str:
        """Return raw RSS/Atom XML text for a feed URL."""
        ...

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from substack_sync.models import MarkdownDocument, Slug


class PostRepository(Protocol):
    def existing_slug_values(self) -> frozenset[str]:
        """Return existing slug values already persisted."""
        ...

    def save_post(self, slug: Slug, document: MarkdownDocument) -> Path:
        """Persist markdown and return saved path."""
        ...

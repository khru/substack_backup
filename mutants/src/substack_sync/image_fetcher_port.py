from __future__ import annotations

from typing import Protocol


class ImageFetcher(Protocol):
    def fetch(self, image_url: str) -> bytes:
        """Return downloaded bytes for a remote image URL."""
        ...

from __future__ import annotations

from pathlib import Path
from typing import Protocol


class ImageBackupRepository(Protocol):
    def has_image(self, markdown_file_path: Path, image_url: str, image_index: int) -> bool:
        """Return True when the target image already exists and is non-empty."""
        ...

    def save_image(
        self,
        markdown_file_path: Path,
        image_url: str,
        image_index: int,
        image_content: bytes,
    ) -> Path:
        """Persist image bytes and return saved path."""
        ...

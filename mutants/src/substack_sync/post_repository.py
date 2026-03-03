from __future__ import annotations

import os
import tempfile
from pathlib import Path

from substack_sync.errors import EmptyMarkdownError, PostPersistenceError
from substack_sync.models import MarkdownDocument, Slug


class FileSystemPostRepository:
    def __init__(self, output_directory: Path) -> None:
        self._output_directory = output_directory

    def existing_slug_values(self) -> frozenset[str]:
        if not self._output_directory.exists():
            return frozenset()

        return frozenset(
            post_path.stem
            for post_path in self._output_directory.glob("*.md")
            if post_path.is_file()
        )

    def save_post(self, slug: Slug, document: MarkdownDocument) -> Path:
        self._output_directory.mkdir(parents=True, exist_ok=True)
        target_path = self._path_for_slug(slug)

        file_descriptor, temp_path_as_text = tempfile.mkstemp(
            prefix=f"{slug.value}-",
            suffix=".tmp",
            dir=self._output_directory,
        )
        temp_path = Path(temp_path_as_text)

        try:
            with os.fdopen(file_descriptor, "w", encoding="utf-8") as stream:
                stream.write(document.content)

            if temp_path.stat().st_size <= 0:
                raise EmptyMarkdownError(f"Generated markdown for {slug.value} is empty.")

            temp_path.replace(target_path)
        except OSError as error:
            raise PostPersistenceError(
                f"Unable to persist markdown for slug {slug.value}"
            ) from error
        finally:
            if temp_path.exists():
                temp_path.unlink()

        return target_path

    def _path_for_slug(self, slug: Slug) -> Path:
        return self._output_directory / slug.to_file_name()

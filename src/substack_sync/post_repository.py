from __future__ import annotations

import hashlib
import os
import re
import tempfile
from pathlib import Path

from substack_sync.errors import EmptyMarkdownError, PostPersistenceError
from substack_sync.models import MarkdownDocument, Slug

_TIMESTAMPED_STEM_PATTERN = re.compile(r"^(?P<timestamp>\d{14})-(?P<slug>[a-z0-9-]+)$")


class FileSystemPostRepository:
    def __init__(self, output_directory: Path) -> None:
        self._output_directory = output_directory

    def existing_slug_values(self) -> frozenset[str]:
        if not self._output_directory.exists():
            return frozenset()

        return frozenset(
            slug_value
            for post_path in self._output_directory.glob("*.md")
            if post_path.is_file()
            if (slug_value := self._slug_value_for_path(post_path)) is not None
        )

    def save_post(self, slug: Slug, document: MarkdownDocument) -> Path:
        self._output_directory.mkdir(parents=True, exist_ok=True)
        target_path = self._path_for_slug(slug)
        self._write_document_to_path(target_path=target_path, slug=slug, document=document)

        return target_path

    def upsert_post(self, slug: Slug, published_timestamp: str, document: MarkdownDocument) -> bool:
        self._output_directory.mkdir(parents=True, exist_ok=True)
        target_path = self._path_for_timestamped_slug(
            slug=slug, published_timestamp=published_timestamp
        )
        existing_paths = self._paths_for_slug(slug)
        preferred_existing_path = self._preferred_existing_path(
            existing_paths=existing_paths,
            target_path=target_path,
        )

        incoming_hash = _content_hash(document.content)
        if preferred_existing_path is not None:
            existing_hash = _content_hash(preferred_existing_path.read_text(encoding="utf-8"))
            if existing_hash == incoming_hash:
                return self._align_paths(
                    preferred_existing_path=preferred_existing_path,
                    target_path=target_path,
                    existing_paths=existing_paths,
                )

        self._write_document_to_path(target_path=target_path, slug=slug, document=document)
        self._remove_duplicate_paths(existing_paths=existing_paths, keep_path=target_path)
        return True

    def _write_document_to_path(
        self, target_path: Path, slug: Slug, document: MarkdownDocument
    ) -> None:
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

    def _align_paths(
        self,
        preferred_existing_path: Path,
        target_path: Path,
        existing_paths: tuple[Path, ...],
    ) -> bool:
        changed = False

        if preferred_existing_path != target_path:
            if target_path.exists():
                target_path.unlink()
            preferred_existing_path.replace(target_path)
            changed = True

        removed_duplicates = self._remove_duplicate_paths(
            existing_paths=existing_paths, keep_path=target_path
        )
        return changed or removed_duplicates

    def _remove_duplicate_paths(self, existing_paths: tuple[Path, ...], keep_path: Path) -> bool:
        removed_duplicates = False
        for existing_path in existing_paths:
            if existing_path == keep_path or not existing_path.exists():
                continue
            existing_path.unlink()
            removed_duplicates = True

        return removed_duplicates

    def _paths_for_slug(self, slug: Slug) -> tuple[Path, ...]:
        if not self._output_directory.exists():
            return ()

        matching_paths = [
            post_path
            for post_path in self._output_directory.glob("*.md")
            if post_path.is_file() and self._slug_value_for_path(post_path) == slug.value
        ]
        return tuple(sorted(matching_paths))

    def _preferred_existing_path(
        self, existing_paths: tuple[Path, ...], target_path: Path
    ) -> Path | None:
        if not existing_paths:
            return None

        if target_path in existing_paths:
            return target_path

        timestamped_paths = [
            path
            for path in existing_paths
            if _TIMESTAMPED_STEM_PATTERN.match(path.stem) is not None
        ]
        if timestamped_paths:
            return max(timestamped_paths)

        return existing_paths[0]

    def _path_for_timestamped_slug(self, slug: Slug, published_timestamp: str) -> Path:
        return self._output_directory / f"{published_timestamp}-{slug.to_file_name()}"

    def _slug_value_for_path(self, post_path: Path) -> str | None:
        if post_path.suffix != ".md":
            return None

        stem = post_path.stem
        if _TIMESTAMPED_STEM_PATTERN.match(stem) is None:
            return stem

        match = _TIMESTAMPED_STEM_PATTERN.match(stem)
        if match is None:
            return None

        return str(match.group("slug"))

    def _path_for_slug(self, slug: Slug) -> Path:
        return self._output_directory / slug.to_file_name()


def _content_hash(content: str) -> str:
    return hashlib.md5(content.encode("utf-8"), usedforsecurity=False).hexdigest()

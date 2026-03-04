from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from substack_sync.errors import EmptyMarkdownError
from substack_sync.models import MarkdownDocument, Slug
from substack_sync.post_repository import FileSystemPostRepository


class FileSystemPostRepositoryTests(unittest.TestCase):
    def test_save_post_persists_markdown_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))

            saved_path = repository.save_post(
                slug=Slug("hello-world"),
                document=MarkdownDocument.from_raw_text("# Hello world"),
            )

            self.assertTrue(saved_path.exists())
            self.assertEqual(saved_path.read_text(encoding="utf-8"), "# Hello world\n")

    def test_existing_slug_values_is_empty_for_new_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))

            self.assertEqual(repository.existing_slug_values(), frozenset())

    def test_markdown_document_disallows_empty_content(self) -> None:
        with self.assertRaises(EmptyMarkdownError):
            MarkdownDocument(content="   ")

    def test_existing_slug_values_returns_saved_markdown_stems(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))
            repository.save_post(
                slug=Slug("first-post"),
                document=MarkdownDocument.from_raw_text("first"),
            )
            repository.save_post(
                slug=Slug("second-post"),
                document=MarkdownDocument.from_raw_text("second"),
            )

            existing_slugs = repository.existing_slug_values()

            self.assertEqual(existing_slugs, frozenset({"first-post", "second-post"}))

    def test_upsert_post_migrates_legacy_file_name_without_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))
            repository.save_post(
                slug=Slug("first-post"),
                document=MarkdownDocument.from_raw_text("first"),
            )

            was_changed = repository.upsert_post(
                slug=Slug("first-post"),
                published_timestamp="20260304070000",
                document=MarkdownDocument.from_raw_text("first"),
            )

            self.assertTrue(was_changed)
            self.assertFalse((Path(temp_directory) / "first-post.md").exists())
            self.assertTrue((Path(temp_directory) / "20260304070000-first-post.md").exists())

    def test_upsert_post_keeps_file_when_content_hash_is_equal(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))

            first_result = repository.upsert_post(
                slug=Slug("second-post"),
                published_timestamp="20260304070100",
                document=MarkdownDocument.from_raw_text("same"),
            )
            second_result = repository.upsert_post(
                slug=Slug("second-post"),
                published_timestamp="20260304070100",
                document=MarkdownDocument.from_raw_text("same"),
            )

            self.assertTrue(first_result)
            self.assertFalse(second_result)


if __name__ == "__main__":
    unittest.main()

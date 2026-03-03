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


if __name__ == "__main__":
    unittest.main()

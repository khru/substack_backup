from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from substack_sync.backup_markdown_images_use_case import BackupMarkdownImagesUseCase
from substack_sync.file_system_image_backup_repository import FileSystemImageBackupRepository
from substack_sync.image_backup_summary import ImageBackupSummary
from substack_sync.image_download_error import ImageDownloadError


class FakeImageFetcher:
    def __init__(
        self,
        image_bytes_by_url: dict[str, bytes],
        failing_urls: set[str] | None = None,
    ) -> None:
        self._image_bytes_by_url = image_bytes_by_url
        self._failing_urls = failing_urls or set()
        self.requested_urls: list[str] = []

    def fetch(self, image_url: str) -> bytes:
        self.requested_urls.append(image_url)

        if image_url in self._failing_urls:
            raise ImageDownloadError(f"Unable to download image from {image_url}")

        return self._image_bytes_by_url[image_url]


class ImageBackupUseCaseTests(unittest.TestCase):
    def test_backup_downloads_images_for_each_post_markdown_file(self) -> None:
        markdown_content = (
            "# Post\n"
            "![](https://example.com/assets/cover.png)\n"
            "[![](https://example.com/assets/chart.jpeg)](https://example.com/post)\n"
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            posts_directory = Path(temp_directory) / "posts"
            posts_directory.mkdir()
            post_path = posts_directory / "20260304070000-example-post.md"
            post_path.write_text(markdown_content, encoding="utf-8")
            image_directory = Path(temp_directory) / "img"

            summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=FakeImageFetcher(
                    image_bytes_by_url={
                        "https://example.com/assets/cover.png": b"cover",
                        "https://example.com/assets/chart.jpeg": b"chart",
                    }
                ),
                image_repository=FileSystemImageBackupRepository(output_directory=image_directory),
            ).backup()

            self.assertEqual(
                summary,
                ImageBackupSummary(
                    total_posts=1,
                    images_discovered=2,
                    downloaded=2,
                    skipped_existing=0,
                    failed=0,
                    failures=(),
                ),
            )
            self.assertEqual(
                len(list((image_directory / "20260304070000-example-post").glob("*"))),
                2,
            )
            self.assertEqual(post_path.read_text(encoding="utf-8"), markdown_content)

    def test_backup_is_idempotent_when_images_already_exist(self) -> None:
        markdown_content = "![](https://example.com/assets/cover.png)\n"
        image_url = "https://example.com/assets/cover.png"

        with tempfile.TemporaryDirectory() as temp_directory:
            posts_directory = Path(temp_directory) / "posts"
            posts_directory.mkdir()
            (posts_directory / "20260304070000-example-post.md").write_text(
                markdown_content,
                encoding="utf-8",
            )
            image_directory = Path(temp_directory) / "img"
            repository = FileSystemImageBackupRepository(output_directory=image_directory)

            first_summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=FakeImageFetcher(image_bytes_by_url={image_url: b"cover"}),
                image_repository=repository,
            ).backup()
            second_fetcher = FakeImageFetcher(image_bytes_by_url={})
            second_summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=second_fetcher,
                image_repository=repository,
            ).backup()

            self.assertEqual(first_summary.downloaded, 1)
            self.assertEqual(second_summary.downloaded, 0)
            self.assertEqual(second_summary.skipped_existing, 1)
            self.assertEqual(second_fetcher.requested_urls, [])

    def test_backup_reports_failures_and_continues_processing_remaining_images(self) -> None:
        markdown_content = (
            "![](https://example.com/assets/cover.png)\n"
            "![](https://example.com/assets/missing.png)\n"
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            posts_directory = Path(temp_directory) / "posts"
            posts_directory.mkdir()
            (posts_directory / "20260304070000-example-post.md").write_text(
                markdown_content,
                encoding="utf-8",
            )
            image_directory = Path(temp_directory) / "img"

            summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=FakeImageFetcher(
                    image_bytes_by_url={"https://example.com/assets/cover.png": b"cover"},
                    failing_urls={"https://example.com/assets/missing.png"},
                ),
                image_repository=FileSystemImageBackupRepository(output_directory=image_directory),
            ).backup()

            self.assertEqual(summary.downloaded, 1)
            self.assertEqual(summary.failed, 1)
            self.assertTrue(summary.has_failures)
            self.assertIn("Unable to download image", summary.failures[0])

    def test_backup_does_not_create_image_directory_when_no_images_exist(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            posts_directory = Path(temp_directory) / "posts"
            posts_directory.mkdir()
            (posts_directory / "20260304070000-example-post.md").write_text(
                "# No images",
                encoding="utf-8",
            )
            image_directory = Path(temp_directory) / "img"

            summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=FakeImageFetcher(image_bytes_by_url={}),
                image_repository=FileSystemImageBackupRepository(output_directory=image_directory),
            ).backup()

            self.assertEqual(summary.images_discovered, 0)
            self.assertFalse(image_directory.exists())

    def test_backup_returns_empty_summary_when_posts_directory_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            posts_directory = Path(temp_directory) / "posts"
            image_directory = Path(temp_directory) / "img"

            summary = BackupMarkdownImagesUseCase(
                posts_directory=posts_directory,
                image_fetcher=FakeImageFetcher(image_bytes_by_url={}),
                image_repository=FileSystemImageBackupRepository(output_directory=image_directory),
            ).backup()

            self.assertEqual(
                summary,
                ImageBackupSummary(
                    total_posts=0,
                    images_discovered=0,
                    downloaded=0,
                    skipped_existing=0,
                    failed=0,
                    failures=(),
                ),
            )


if __name__ == "__main__":
    unittest.main()

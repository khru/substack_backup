from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from substack_sync.archive_parser import ArchivePost
from substack_sync.archive_use_case import SyncSubstackArchivePostsUseCase
from substack_sync.errors import MarkdownDownloadError
from substack_sync.models import MarkdownDocument, Slug, SyncSummary
from substack_sync.post_repository import FileSystemPostRepository


class FakeArchiveReader:
    def __init__(self, posts: tuple[ArchivePost, ...]) -> None:
        self._posts = posts
        self.received_archive_urls: list[str] = []

    def fetch(self, archive_url: str) -> tuple[ArchivePost, ...]:
        self.received_archive_urls.append(archive_url)
        return self._posts


class FakeMarkdownFetcher:
    def __init__(
        self,
        markdown_by_url: dict[str, str],
        failing_urls: set[str] | None = None,
    ) -> None:
        self._markdown_by_url = markdown_by_url
        self._failing_urls = failing_urls or set()

    def fetch(self, article_url: str) -> str:
        if article_url in self._failing_urls:
            raise MarkdownDownloadError(f"Unable to download markdown for {article_url}")

        return self._markdown_by_url[article_url]


class ArchiveUseCaseTests(unittest.TestCase):
    def test_sync_fetches_archive_using_received_archive_url(self) -> None:
        requested_archive_url = "https://example.workers.dev/archive"
        archive_reader = FakeArchiveReader(posts=())
        use_case = SyncSubstackArchivePostsUseCase(
            archive_reader=archive_reader,
            markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={}),
            post_repository=FileSystemPostRepository(output_directory=Path(tempfile.gettempdir())),
        )

        use_case.sync(archive_url=requested_archive_url)

        self.assertEqual(archive_reader.received_archive_urls, [requested_archive_url])

    def test_sync_persists_timestamped_post_file_name(self) -> None:
        article_url = "https://example.substack.com/p/new-post"
        archive_post = ArchivePost(
            article_url=article_url,
            published_timestamp="20260304070000",
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            use_case = SyncSubstackArchivePostsUseCase(
                archive_reader=FakeArchiveReader(posts=(archive_post,)),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={article_url: "# New"}),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            summary = use_case.sync(archive_url="https://example.workers.dev/archive")

            self.assertTrue((Path(temp_directory) / "20260304070000-new-post.md").exists())
            self.assertEqual(
                summary,
                SyncSummary(
                    total_urls=1,
                    downloaded=1,
                    skipped_existing=0,
                    failed=0,
                    failures=(),
                ),
            )

    def test_sync_renames_legacy_slug_file_without_duplicates(self) -> None:
        article_url = "https://example.substack.com/p/migrated-post"
        archive_post = ArchivePost(
            article_url=article_url,
            published_timestamp="20260304070100",
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))
            repository.save_post(
                slug=Slug("migrated-post"),
                document=MarkdownDocument.from_raw_text("same"),
            )
            use_case = SyncSubstackArchivePostsUseCase(
                archive_reader=FakeArchiveReader(posts=(archive_post,)),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={article_url: "same"}),
                post_repository=repository,
            )

            summary = use_case.sync(archive_url="https://example.workers.dev/archive")

            self.assertFalse((Path(temp_directory) / "migrated-post.md").exists())
            self.assertTrue((Path(temp_directory) / "20260304070100-migrated-post.md").exists())
            self.assertEqual(summary.downloaded, 1)

    def test_sync_skips_post_when_hash_matches_current_timestamped_file(self) -> None:
        article_url = "https://example.substack.com/p/stable-post"
        archive_post = ArchivePost(
            article_url=article_url,
            published_timestamp="20260304070200",
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))
            repository.upsert_post(
                slug=Slug("stable-post"),
                published_timestamp="20260304070200",
                document=MarkdownDocument.from_raw_text("stable"),
            )
            use_case = SyncSubstackArchivePostsUseCase(
                archive_reader=FakeArchiveReader(posts=(archive_post,)),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={article_url: "stable"}),
                post_repository=repository,
            )

            summary = use_case.sync(archive_url="https://example.workers.dev/archive")

            self.assertEqual(summary.downloaded, 0)
            self.assertEqual(summary.skipped_existing, 1)


if __name__ == "__main__":
    unittest.main()

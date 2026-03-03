from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from substack_sync.errors import MarkdownDownloadError
from substack_sync.models import MarkdownDocument, Slug, SyncSummary
from substack_sync.post_repository import FileSystemPostRepository
from substack_sync.use_case import SyncSubstackPostsUseCase

_FEED_URL = "https://emmanuelvalverderamos.substack.com/feed.xml"


def _build_feed_xml(urls: list[str]) -> str:
    entries = "".join(f"<item><link>{url}</link></item>" for url in urls)
    return f"<?xml version='1.0' encoding='UTF-8'?><rss><channel>{entries}</channel></rss>"


class FakeFeedReader:
    def __init__(self, xml_content: str) -> None:
        self._xml_content = xml_content
        self.received_feed_urls: list[str] = []

    def fetch(self, feed_url: str) -> str:
        self.received_feed_urls.append(feed_url)
        return self._xml_content


class FakeMarkdownFetcher:
    def __init__(
        self, markdown_by_url: dict[str, str], failing_urls: set[str] | None = None
    ) -> None:
        self._markdown_by_url = markdown_by_url
        self._failing_urls = failing_urls or set()

    def fetch(self, article_url: str) -> str:
        if article_url in self._failing_urls:
            raise MarkdownDownloadError(f"Unable to download markdown for {article_url}")

        return self._markdown_by_url[article_url]


class PlanningAwareRepository:
    def __init__(self, output_directory: Path, existing_slug_values: set[str]) -> None:
        self._repository = FileSystemPostRepository(output_directory=output_directory)
        self._existing_slug_values = existing_slug_values

    def existing_slug_values(self) -> frozenset[str]:
        return frozenset(self._existing_slug_values)

    def save_post(self, slug: Slug, document: MarkdownDocument) -> Path:
        return self._repository.save_post(slug=slug, document=document)


class SyncSubstackPostsUseCaseTests(unittest.TestCase):
    def test_sync_fetches_feed_using_received_feed_url(self) -> None:
        requested_feed_url = "https://example.com/custom-feed.xml"
        feed_reader = FakeFeedReader(_build_feed_xml([]))
        use_case = SyncSubstackPostsUseCase(
            feed_reader=feed_reader,
            markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={}),
            post_repository=FileSystemPostRepository(output_directory=Path(tempfile.gettempdir())),
        )

        use_case.sync(feed_url=requested_feed_url)

        self.assertEqual(feed_reader.received_feed_urls, [requested_feed_url])

    def test_downloads_only_new_posts_returns_expected_summary(self) -> None:
        existing_url = "https://emmanuelvalverderamos.substack.com/p/already-saved"
        new_url = "https://emmanuelvalverderamos.substack.com/p/new-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            repository = FileSystemPostRepository(output_directory=Path(temp_directory))
            repository.save_post(
                slug=Slug.from_article_url(existing_url),
                document=MarkdownDocument.from_raw_text("existing"),
            )

            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([existing_url, new_url])),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={new_url: "# New"}),
                post_repository=repository,
            )

            summary = use_case.sync(feed_url=_FEED_URL)

            self.assertEqual(
                summary,
                SyncSummary(
                    total_urls=2,
                    downloaded=1,
                    skipped_existing=1,
                    failed=0,
                    failures=(),
                ),
            )

    def test_downloads_only_new_posts_persists_markdown_file(self) -> None:
        new_url = "https://emmanuelvalverderamos.substack.com/p/new-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([new_url])),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={new_url: "# New"}),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            use_case.sync(feed_url=_FEED_URL)

            self.assertTrue((Path(temp_directory) / "new-post.md").exists())

    def test_marks_failure_when_endpoint_returns_empty_markdown(self) -> None:
        article_url = "https://emmanuelvalverderamos.substack.com/p/empty-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([article_url])),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={article_url: "   "}),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            summary = use_case.sync(feed_url=_FEED_URL)

            self.assertEqual(
                summary,
                SyncSummary(
                    total_urls=1,
                    downloaded=0,
                    skipped_existing=0,
                    failed=1,
                    failures=(
                        "https://emmanuelvalverderamos.substack.com/p/empty-post: "
                        "Markdown content is empty.",
                    ),
                ),
            )

    def test_continues_processing_remaining_urls_after_failure(self) -> None:
        failing_url = "https://emmanuelvalverderamos.substack.com/p/failing-post"
        successful_url = "https://emmanuelvalverderamos.substack.com/p/successful-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([failing_url, successful_url])),
                markdown_fetcher=FakeMarkdownFetcher(
                    markdown_by_url={successful_url: "# Success"},
                    failing_urls={failing_url},
                ),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            summary = use_case.sync(feed_url=_FEED_URL)

            self.assertEqual(
                summary,
                SyncSummary(
                    total_urls=2,
                    downloaded=1,
                    skipped_existing=0,
                    failed=1,
                    failures=(
                        "https://emmanuelvalverderamos.substack.com/p/failing-post: "
                        "Unable to download markdown for "
                        "https://emmanuelvalverderamos.substack.com/p/failing-post",
                    ),
                ),
            )

    def test_continues_processing_persists_successful_url_even_with_failures(self) -> None:
        failing_url = "https://emmanuelvalverderamos.substack.com/p/failing-post"
        successful_url = "https://emmanuelvalverderamos.substack.com/p/successful-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([failing_url, successful_url])),
                markdown_fetcher=FakeMarkdownFetcher(
                    markdown_by_url={successful_url: "# Success"},
                    failing_urls={failing_url},
                ),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            use_case.sync(feed_url=_FEED_URL)

            self.assertTrue((Path(temp_directory) / "successful-post.md").exists())

    def test_uses_existing_slug_snapshot_during_planning(self) -> None:
        existing_url = "https://emmanuelvalverderamos.substack.com/p/already-saved"
        new_url = "https://emmanuelvalverderamos.substack.com/p/new-post"

        with tempfile.TemporaryDirectory() as temp_directory:
            repository = PlanningAwareRepository(
                output_directory=Path(temp_directory),
                existing_slug_values={"already-saved"},
            )
            use_case = SyncSubstackPostsUseCase(
                feed_reader=FakeFeedReader(_build_feed_xml([existing_url, new_url])),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={new_url: "# New"}),
                post_repository=repository,
            )

            summary = use_case.sync(feed_url=_FEED_URL)

            self.assertEqual(
                summary,
                SyncSummary(
                    total_urls=2,
                    downloaded=1,
                    skipped_existing=1,
                    failed=0,
                    failures=(),
                ),
            )


if __name__ == "__main__":
    unittest.main()

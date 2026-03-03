from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from substack_sync.errors import MarkdownDownloadError
from substack_sync.models import Slug
from substack_sync.post_repository import FileSystemPostRepository
from substack_sync.sync_execution import SyncExecutionResult, execute_download_candidates
from substack_sync.sync_planning import DownloadCandidate


class FakeMarkdownFetcher:
    def __init__(
        self, markdown_by_url: dict[str, str], failing_urls: set[str] | None = None
    ) -> None:
        self._markdown_by_url = markdown_by_url
        self._failing_urls = failing_urls or set()

    def fetch(self, article_url: str) -> str:
        if article_url in self._failing_urls:
            raise MarkdownDownloadError(f"unable to download markdown for {article_url}")

        return self._markdown_by_url[article_url]


class UnexpectedErrorMarkdownFetcher:
    def fetch(self, article_url: str) -> str:
        _ = article_url
        raise RuntimeError("unexpected fetch failure")


class SyncExecutionTests(unittest.TestCase):
    def test_execute_download_candidates_returns_expected_summary(self) -> None:
        failing_url = "https://emmanuelvalverderamos.substack.com/p/failing-post"
        successful_url = "https://emmanuelvalverderamos.substack.com/p/successful-post"

        candidates = (
            DownloadCandidate(article_url=failing_url, slug=Slug("failing-post")),
            DownloadCandidate(article_url=successful_url, slug=Slug("successful-post")),
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            result = execute_download_candidates(
                candidates=candidates,
                markdown_fetcher=FakeMarkdownFetcher(
                    markdown_by_url={successful_url: "# Success"},
                    failing_urls={failing_url},
                ),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            self.assertEqual(
                result,
                SyncExecutionResult(
                    downloaded=1,
                    failed=1,
                    failures=(
                        "https://emmanuelvalverderamos.substack.com/p/failing-post: "
                        "unable to download markdown for "
                        "https://emmanuelvalverderamos.substack.com/p/failing-post",
                    ),
                ),
            )

    def test_execute_download_candidates_persists_successful_markdown(self) -> None:
        successful_url = "https://emmanuelvalverderamos.substack.com/p/successful-post"
        candidate = DownloadCandidate(
            article_url=successful_url,
            slug=Slug("successful-post"),
        )

        with tempfile.TemporaryDirectory() as temp_directory:
            execute_download_candidates(
                candidates=(candidate,),
                markdown_fetcher=FakeMarkdownFetcher(markdown_by_url={successful_url: "# Success"}),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )

            self.assertTrue((Path(temp_directory) / "successful-post.md").exists())

    def test_execute_download_candidates_propagates_unexpected_exceptions(self) -> None:
        candidate = DownloadCandidate(
            article_url="https://emmanuelvalverderamos.substack.com/p/post",
            slug=Slug("post"),
        )

        with tempfile.TemporaryDirectory() as temp_directory, self.assertRaises(RuntimeError):
            execute_download_candidates(
                candidates=(candidate,),
                markdown_fetcher=UnexpectedErrorMarkdownFetcher(),
                post_repository=FileSystemPostRepository(output_directory=Path(temp_directory)),
            )


if __name__ == "__main__":
    unittest.main()

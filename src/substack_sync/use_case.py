from __future__ import annotations

from substack_sync.models import SyncSummary
from substack_sync.ports import FeedReader, MarkdownFetcher, PostRepository
from substack_sync.rss_parser import extract_article_urls
from substack_sync.sync_execution import execute_download_candidates
from substack_sync.sync_planning import build_sync_plan


class SyncSubstackPostsUseCase:
    def __init__(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        self._feed_reader = feed_reader
        self._markdown_fetcher = markdown_fetcher
        self._post_repository = post_repository

    def sync(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = execute_download_candidates(
            candidates=plan.download_candidates,
            markdown_fetcher=self._markdown_fetcher,
            post_repository=self._post_repository,
        )

        failures = _combine_failures(plan.rejected_urls, execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )


def _combine_failures(
    planning_failures: tuple[str, ...],
    execution_failures: tuple[str, ...],
) -> tuple[str, ...]:
    return (*planning_failures, *execution_failures)

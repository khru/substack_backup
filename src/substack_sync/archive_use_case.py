from __future__ import annotations

from substack_sync.errors import SubstackSyncError
from substack_sync.models import MarkdownDocument, Slug, SyncSummary
from substack_sync.ports import ArchivePostRepository, ArchiveReader, MarkdownFetcher


class SyncSubstackArchivePostsUseCase:
    def __init__(
        self,
        archive_reader: ArchiveReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: ArchivePostRepository,
    ) -> None:
        self._archive_reader = archive_reader
        self._markdown_fetcher = markdown_fetcher
        self._post_repository = post_repository

    def sync(self, archive_url: str) -> SyncSummary:
        archive_posts = self._archive_reader.fetch(archive_url)

        downloaded = 0
        skipped_existing = 0
        failures: list[str] = []

        for archive_post in archive_posts:
            try:
                slug = Slug.from_article_url(archive_post.article_url)
                markdown_text = self._markdown_fetcher.fetch(archive_post.article_url)
                document = MarkdownDocument.from_raw_text(markdown_text)
                was_changed = self._post_repository.upsert_post(
                    slug=slug,
                    published_timestamp=archive_post.published_timestamp,
                    document=document,
                )
            except SubstackSyncError as error:
                failures.append(f"{archive_post.article_url}: {error}")
                continue

            if was_changed:
                downloaded += 1
            else:
                skipped_existing += 1

        return SyncSummary(
            total_urls=len(archive_posts),
            downloaded=downloaded,
            skipped_existing=skipped_existing,
            failed=len(failures),
            failures=tuple(failures),
        )

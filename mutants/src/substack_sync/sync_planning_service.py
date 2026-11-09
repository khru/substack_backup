from __future__ import annotations

from collections.abc import Sequence

from substack_sync.download_candidate import DownloadCandidate
from substack_sync.invalid_article_url_error import InvalidArticleUrlError
from substack_sync.models import Slug
from substack_sync.rejected_slug import RejectedSlug
from substack_sync.resolved_slug import ResolvedSlug
from substack_sync.slug_resolution import SlugResolution
from substack_sync.sync_plan import SyncPlan


def build_sync_plan(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            continue

        if resolution.slug.value in existing_slug_values:
            skipped_existing += 1
            continue

        candidates.append(
            DownloadCandidate(article_url=resolution.article_url, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def resolve_slug(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, slug=slug)

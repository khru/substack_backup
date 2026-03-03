from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from substack_sync.errors import InvalidArticleUrlError
from substack_sync.models import Slug


@dataclass(frozen=True)
class DownloadCandidate:
    article_url: str
    slug: Slug


@dataclass(frozen=True)
class SyncPlan:
    download_candidates: tuple[DownloadCandidate, ...]
    skipped_existing: int
    rejected_urls: tuple[str, ...]


@dataclass(frozen=True)
class ResolvedSlug:
    article_url: str
    slug: Slug


@dataclass(frozen=True)
class RejectedSlug:
    reason: str


SlugResolution = ResolvedSlug | RejectedSlug


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

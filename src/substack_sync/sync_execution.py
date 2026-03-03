from __future__ import annotations

from dataclasses import dataclass

from substack_sync.errors import SubstackSyncError
from substack_sync.models import MarkdownDocument
from substack_sync.ports import MarkdownFetcher, PostRepository
from substack_sync.sync_planning import DownloadCandidate


@dataclass(frozen=True)
class DownloadSucceeded:
    pass


@dataclass(frozen=True)
class DownloadFailed:
    reason: str


DownloadOutcome = DownloadSucceeded | DownloadFailed


@dataclass(frozen=True)
class SyncExecutionResult:
    downloaded: int
    failed: int
    failures: tuple[str, ...]


def execute_download_candidates(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=candidate,
            markdown_fetcher=markdown_fetcher,
            post_repository=post_repository,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def _download_candidate(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def _summarize_outcomes(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )

from __future__ import annotations

from substack_sync.download_failed import DownloadFailed
from substack_sync.download_outcome import DownloadOutcome
from substack_sync.download_succeeded import DownloadSucceeded
from substack_sync.markdown_document import MarkdownDocument
from substack_sync.ports import MarkdownFetcher, PostRepository
from substack_sync.substack_sync_error import SubstackSyncError
from substack_sync.sync_execution_result import SyncExecutionResult
from substack_sync.sync_planning import DownloadCandidate


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

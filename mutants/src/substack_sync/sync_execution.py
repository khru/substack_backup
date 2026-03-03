from __future__ import annotations

from dataclasses import dataclass

from substack_sync.errors import SubstackSyncError
from substack_sync.models import MarkdownDocument
from substack_sync.ports import MarkdownFetcher, PostRepository
from substack_sync.sync_planning import DownloadCandidate
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


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
    args = [candidates, markdown_fetcher, post_repository]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_execute_download_candidates__mutmut_orig, x_execute_download_candidates__mutmut_mutants, args, kwargs, None)


def x_execute_download_candidates__mutmut_orig(
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


def x_execute_download_candidates__mutmut_1(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = None
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_2(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        None
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_3(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=None,
            markdown_fetcher=markdown_fetcher,
            post_repository=post_repository,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_4(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=candidate,
            markdown_fetcher=None,
            post_repository=post_repository,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_5(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=candidate,
            markdown_fetcher=markdown_fetcher,
            post_repository=None,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_6(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            markdown_fetcher=markdown_fetcher,
            post_repository=post_repository,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_7(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=candidate,
            post_repository=post_repository,
        )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_8(
    candidates: tuple[DownloadCandidate, ...],
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> SyncExecutionResult:
    outcomes = tuple(
        _download_candidate(
            candidate=candidate,
            markdown_fetcher=markdown_fetcher,
            )
        for candidate in candidates
    )
    return _summarize_outcomes(outcomes)


def x_execute_download_candidates__mutmut_9(
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
    return _summarize_outcomes(None)

x_execute_download_candidates__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_execute_download_candidates__mutmut_1': x_execute_download_candidates__mutmut_1, 
    'x_execute_download_candidates__mutmut_2': x_execute_download_candidates__mutmut_2, 
    'x_execute_download_candidates__mutmut_3': x_execute_download_candidates__mutmut_3, 
    'x_execute_download_candidates__mutmut_4': x_execute_download_candidates__mutmut_4, 
    'x_execute_download_candidates__mutmut_5': x_execute_download_candidates__mutmut_5, 
    'x_execute_download_candidates__mutmut_6': x_execute_download_candidates__mutmut_6, 
    'x_execute_download_candidates__mutmut_7': x_execute_download_candidates__mutmut_7, 
    'x_execute_download_candidates__mutmut_8': x_execute_download_candidates__mutmut_8, 
    'x_execute_download_candidates__mutmut_9': x_execute_download_candidates__mutmut_9
}
x_execute_download_candidates__mutmut_orig.__name__ = 'x_execute_download_candidates'


def _download_candidate(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    args = [candidate, markdown_fetcher, post_repository]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__download_candidate__mutmut_orig, x__download_candidate__mutmut_mutants, args, kwargs, None)


def x__download_candidate__mutmut_orig(
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


def x__download_candidate__mutmut_1(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = None
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_2(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(None)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_3(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = None
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_4(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(None)
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_5(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(None, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_6(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, None)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_7(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_8(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, )
    except SubstackSyncError as error:
        return DownloadFailed(reason=f"{candidate.article_url}: {error}")

    return DownloadSucceeded()


def x__download_candidate__mutmut_9(
    candidate: DownloadCandidate,
    markdown_fetcher: MarkdownFetcher,
    post_repository: PostRepository,
) -> DownloadOutcome:
    try:
        markdown_text = markdown_fetcher.fetch(candidate.article_url)
        document = MarkdownDocument.from_raw_text(markdown_text)
        post_repository.save_post(candidate.slug, document)
    except SubstackSyncError as error:
        return DownloadFailed(reason=None)

    return DownloadSucceeded()

x__download_candidate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__download_candidate__mutmut_1': x__download_candidate__mutmut_1, 
    'x__download_candidate__mutmut_2': x__download_candidate__mutmut_2, 
    'x__download_candidate__mutmut_3': x__download_candidate__mutmut_3, 
    'x__download_candidate__mutmut_4': x__download_candidate__mutmut_4, 
    'x__download_candidate__mutmut_5': x__download_candidate__mutmut_5, 
    'x__download_candidate__mutmut_6': x__download_candidate__mutmut_6, 
    'x__download_candidate__mutmut_7': x__download_candidate__mutmut_7, 
    'x__download_candidate__mutmut_8': x__download_candidate__mutmut_8, 
    'x__download_candidate__mutmut_9': x__download_candidate__mutmut_9
}
x__download_candidate__mutmut_orig.__name__ = 'x__download_candidate'


def _summarize_outcomes(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    args = [outcomes]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__summarize_outcomes__mutmut_orig, x__summarize_outcomes__mutmut_mutants, args, kwargs, None)


def x__summarize_outcomes__mutmut_orig(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_1(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = None
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_2(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(None)
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_3(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=None,
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_4(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=None,
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_5(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=None,
    )


def x__summarize_outcomes__mutmut_6(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_7(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_8(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        )


def x__summarize_outcomes__mutmut_9(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) + len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(outcome.reason for outcome in failed_outcomes),
    )


def x__summarize_outcomes__mutmut_10(outcomes: tuple[DownloadOutcome, ...]) -> SyncExecutionResult:
    failed_outcomes = tuple(outcome for outcome in outcomes if isinstance(outcome, DownloadFailed))
    return SyncExecutionResult(
        downloaded=len(outcomes) - len(failed_outcomes),
        failed=len(failed_outcomes),
        failures=tuple(None),
    )

x__summarize_outcomes__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__summarize_outcomes__mutmut_1': x__summarize_outcomes__mutmut_1, 
    'x__summarize_outcomes__mutmut_2': x__summarize_outcomes__mutmut_2, 
    'x__summarize_outcomes__mutmut_3': x__summarize_outcomes__mutmut_3, 
    'x__summarize_outcomes__mutmut_4': x__summarize_outcomes__mutmut_4, 
    'x__summarize_outcomes__mutmut_5': x__summarize_outcomes__mutmut_5, 
    'x__summarize_outcomes__mutmut_6': x__summarize_outcomes__mutmut_6, 
    'x__summarize_outcomes__mutmut_7': x__summarize_outcomes__mutmut_7, 
    'x__summarize_outcomes__mutmut_8': x__summarize_outcomes__mutmut_8, 
    'x__summarize_outcomes__mutmut_9': x__summarize_outcomes__mutmut_9, 
    'x__summarize_outcomes__mutmut_10': x__summarize_outcomes__mutmut_10
}
x__summarize_outcomes__mutmut_orig.__name__ = 'x__summarize_outcomes'

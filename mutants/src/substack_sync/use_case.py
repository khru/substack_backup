from __future__ import annotations

from substack_sync.models import SyncSummary
from substack_sync.ports import FeedReader, MarkdownFetcher, PostRepository
from substack_sync.rss_parser import extract_article_urls
from substack_sync.sync_execution import execute_download_candidates
from substack_sync.sync_planning import build_sync_plan
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


class SyncSubstackPostsUseCase:
    def __init__(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        args = [feed_reader, markdown_fetcher, post_repository]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSyncSubstackPostsUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁSyncSubstackPostsUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁSyncSubstackPostsUseCaseǁ__init____mutmut_orig(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        self._feed_reader = feed_reader
        self._markdown_fetcher = markdown_fetcher
        self._post_repository = post_repository
    def xǁSyncSubstackPostsUseCaseǁ__init____mutmut_1(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        self._feed_reader = None
        self._markdown_fetcher = markdown_fetcher
        self._post_repository = post_repository
    def xǁSyncSubstackPostsUseCaseǁ__init____mutmut_2(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        self._feed_reader = feed_reader
        self._markdown_fetcher = None
        self._post_repository = post_repository
    def xǁSyncSubstackPostsUseCaseǁ__init____mutmut_3(
        self,
        feed_reader: FeedReader,
        markdown_fetcher: MarkdownFetcher,
        post_repository: PostRepository,
    ) -> None:
        self._feed_reader = feed_reader
        self._markdown_fetcher = markdown_fetcher
        self._post_repository = None
    
    xǁSyncSubstackPostsUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSyncSubstackPostsUseCaseǁ__init____mutmut_1': xǁSyncSubstackPostsUseCaseǁ__init____mutmut_1, 
        'xǁSyncSubstackPostsUseCaseǁ__init____mutmut_2': xǁSyncSubstackPostsUseCaseǁ__init____mutmut_2, 
        'xǁSyncSubstackPostsUseCaseǁ__init____mutmut_3': xǁSyncSubstackPostsUseCaseǁ__init____mutmut_3
    }
    xǁSyncSubstackPostsUseCaseǁ__init____mutmut_orig.__name__ = 'xǁSyncSubstackPostsUseCaseǁ__init__'

    def sync(self, feed_url: str) -> SyncSummary:
        args = [feed_url]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSyncSubstackPostsUseCaseǁsync__mutmut_orig'), object.__getattribute__(self, 'xǁSyncSubstackPostsUseCaseǁsync__mutmut_mutants'), args, kwargs, self)

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_orig(self, feed_url: str) -> SyncSummary:
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_1(self, feed_url: str) -> SyncSummary:
        feed_xml = None
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_2(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(None)
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_3(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = None

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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_4(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(None)

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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_5(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(None))

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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_6(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = None
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_7(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = None
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_8(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=None,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_9(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=None,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_10(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_11(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_12(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = None

        failures = _combine_failures(plan.rejected_urls, execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_13(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = execute_download_candidates(
            candidates=None,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_14(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = execute_download_candidates(
            candidates=plan.download_candidates,
            markdown_fetcher=None,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_15(self, feed_url: str) -> SyncSummary:
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
            post_repository=None,
        )

        failures = _combine_failures(plan.rejected_urls, execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_16(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = execute_download_candidates(
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_17(self, feed_url: str) -> SyncSummary:
        feed_xml = self._feed_reader.fetch(feed_url)
        article_urls = tuple(extract_article_urls(feed_xml))

        existing_slug_values = self._post_repository.existing_slug_values()
        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=existing_slug_values,
        )
        execution_result = execute_download_candidates(
            candidates=plan.download_candidates,
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

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_18(self, feed_url: str) -> SyncSummary:
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
            )

        failures = _combine_failures(plan.rejected_urls, execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_19(self, feed_url: str) -> SyncSummary:
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

        failures = None

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_20(self, feed_url: str) -> SyncSummary:
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

        failures = _combine_failures(None, execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_21(self, feed_url: str) -> SyncSummary:
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

        failures = _combine_failures(plan.rejected_urls, None)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_22(self, feed_url: str) -> SyncSummary:
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

        failures = _combine_failures(execution_result.failures)

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_23(self, feed_url: str) -> SyncSummary:
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

        failures = _combine_failures(plan.rejected_urls, )

        return SyncSummary(
            total_urls=len(article_urls),
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_24(self, feed_url: str) -> SyncSummary:
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
            total_urls=None,
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_25(self, feed_url: str) -> SyncSummary:
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
            downloaded=None,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_26(self, feed_url: str) -> SyncSummary:
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
            skipped_existing=None,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_27(self, feed_url: str) -> SyncSummary:
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
            failed=None,
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_28(self, feed_url: str) -> SyncSummary:
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
            failures=None,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_29(self, feed_url: str) -> SyncSummary:
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
            downloaded=execution_result.downloaded,
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_30(self, feed_url: str) -> SyncSummary:
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
            skipped_existing=plan.skipped_existing,
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_31(self, feed_url: str) -> SyncSummary:
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
            failed=len(failures),
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_32(self, feed_url: str) -> SyncSummary:
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
            failures=failures,
        )

    def xǁSyncSubstackPostsUseCaseǁsync__mutmut_33(self, feed_url: str) -> SyncSummary:
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
            )
    
    xǁSyncSubstackPostsUseCaseǁsync__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSyncSubstackPostsUseCaseǁsync__mutmut_1': xǁSyncSubstackPostsUseCaseǁsync__mutmut_1, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_2': xǁSyncSubstackPostsUseCaseǁsync__mutmut_2, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_3': xǁSyncSubstackPostsUseCaseǁsync__mutmut_3, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_4': xǁSyncSubstackPostsUseCaseǁsync__mutmut_4, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_5': xǁSyncSubstackPostsUseCaseǁsync__mutmut_5, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_6': xǁSyncSubstackPostsUseCaseǁsync__mutmut_6, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_7': xǁSyncSubstackPostsUseCaseǁsync__mutmut_7, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_8': xǁSyncSubstackPostsUseCaseǁsync__mutmut_8, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_9': xǁSyncSubstackPostsUseCaseǁsync__mutmut_9, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_10': xǁSyncSubstackPostsUseCaseǁsync__mutmut_10, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_11': xǁSyncSubstackPostsUseCaseǁsync__mutmut_11, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_12': xǁSyncSubstackPostsUseCaseǁsync__mutmut_12, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_13': xǁSyncSubstackPostsUseCaseǁsync__mutmut_13, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_14': xǁSyncSubstackPostsUseCaseǁsync__mutmut_14, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_15': xǁSyncSubstackPostsUseCaseǁsync__mutmut_15, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_16': xǁSyncSubstackPostsUseCaseǁsync__mutmut_16, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_17': xǁSyncSubstackPostsUseCaseǁsync__mutmut_17, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_18': xǁSyncSubstackPostsUseCaseǁsync__mutmut_18, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_19': xǁSyncSubstackPostsUseCaseǁsync__mutmut_19, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_20': xǁSyncSubstackPostsUseCaseǁsync__mutmut_20, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_21': xǁSyncSubstackPostsUseCaseǁsync__mutmut_21, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_22': xǁSyncSubstackPostsUseCaseǁsync__mutmut_22, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_23': xǁSyncSubstackPostsUseCaseǁsync__mutmut_23, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_24': xǁSyncSubstackPostsUseCaseǁsync__mutmut_24, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_25': xǁSyncSubstackPostsUseCaseǁsync__mutmut_25, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_26': xǁSyncSubstackPostsUseCaseǁsync__mutmut_26, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_27': xǁSyncSubstackPostsUseCaseǁsync__mutmut_27, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_28': xǁSyncSubstackPostsUseCaseǁsync__mutmut_28, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_29': xǁSyncSubstackPostsUseCaseǁsync__mutmut_29, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_30': xǁSyncSubstackPostsUseCaseǁsync__mutmut_30, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_31': xǁSyncSubstackPostsUseCaseǁsync__mutmut_31, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_32': xǁSyncSubstackPostsUseCaseǁsync__mutmut_32, 
        'xǁSyncSubstackPostsUseCaseǁsync__mutmut_33': xǁSyncSubstackPostsUseCaseǁsync__mutmut_33
    }
    xǁSyncSubstackPostsUseCaseǁsync__mutmut_orig.__name__ = 'xǁSyncSubstackPostsUseCaseǁsync'


def _combine_failures(
    planning_failures: tuple[str, ...],
    execution_failures: tuple[str, ...],
) -> tuple[str, ...]:
    return (*planning_failures, *execution_failures)

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from substack_sync.errors import InvalidArticleUrlError
from substack_sync.models import Slug
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
    args = [article_urls, existing_slug_values]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_build_sync_plan__mutmut_orig, x_build_sync_plan__mutmut_mutants, args, kwargs, None)


def x_build_sync_plan__mutmut_orig(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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


def x_build_sync_plan__mutmut_1(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = None
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


def x_build_sync_plan__mutmut_2(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = None
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


def x_build_sync_plan__mutmut_3(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = None

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


def x_build_sync_plan__mutmut_4(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 1

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


def x_build_sync_plan__mutmut_5(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = None
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


def x_build_sync_plan__mutmut_6(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(None)
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


def x_build_sync_plan__mutmut_7(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(None)
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


def x_build_sync_plan__mutmut_8(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            break

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


def x_build_sync_plan__mutmut_9(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            continue

        if resolution.slug.value not in existing_slug_values:
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


def x_build_sync_plan__mutmut_10(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            continue

        if resolution.slug.value in existing_slug_values:
            skipped_existing = 1
            continue

        candidates.append(
            DownloadCandidate(article_url=resolution.article_url, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_11(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            continue

        if resolution.slug.value in existing_slug_values:
            skipped_existing -= 1
            continue

        candidates.append(
            DownloadCandidate(article_url=resolution.article_url, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_12(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
    candidates: list[DownloadCandidate] = []
    rejected_urls: list[str] = []
    skipped_existing = 0

    for article_url in article_urls:
        resolution = resolve_slug(article_url)
        if isinstance(resolution, RejectedSlug):
            rejected_urls.append(resolution.reason)
            continue

        if resolution.slug.value in existing_slug_values:
            skipped_existing += 2
            continue

        candidates.append(
            DownloadCandidate(article_url=resolution.article_url, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_13(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            break

        candidates.append(
            DownloadCandidate(article_url=resolution.article_url, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_14(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            None
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_15(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            DownloadCandidate(article_url=None, slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_16(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            DownloadCandidate(article_url=resolution.article_url, slug=None)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_17(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            DownloadCandidate(slug=resolution.slug)
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_18(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
            DownloadCandidate(article_url=resolution.article_url, )
        )

    return SyncPlan(
        download_candidates=tuple(candidates),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_19(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        download_candidates=None,
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_20(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        skipped_existing=None,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_21(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        rejected_urls=None,
    )


def x_build_sync_plan__mutmut_22(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_23(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_24(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        )


def x_build_sync_plan__mutmut_25(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        download_candidates=tuple(None),
        skipped_existing=skipped_existing,
        rejected_urls=tuple(rejected_urls),
    )


def x_build_sync_plan__mutmut_26(article_urls: Sequence[str], existing_slug_values: frozenset[str]) -> SyncPlan:
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
        rejected_urls=tuple(None),
    )

x_build_sync_plan__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_build_sync_plan__mutmut_1': x_build_sync_plan__mutmut_1, 
    'x_build_sync_plan__mutmut_2': x_build_sync_plan__mutmut_2, 
    'x_build_sync_plan__mutmut_3': x_build_sync_plan__mutmut_3, 
    'x_build_sync_plan__mutmut_4': x_build_sync_plan__mutmut_4, 
    'x_build_sync_plan__mutmut_5': x_build_sync_plan__mutmut_5, 
    'x_build_sync_plan__mutmut_6': x_build_sync_plan__mutmut_6, 
    'x_build_sync_plan__mutmut_7': x_build_sync_plan__mutmut_7, 
    'x_build_sync_plan__mutmut_8': x_build_sync_plan__mutmut_8, 
    'x_build_sync_plan__mutmut_9': x_build_sync_plan__mutmut_9, 
    'x_build_sync_plan__mutmut_10': x_build_sync_plan__mutmut_10, 
    'x_build_sync_plan__mutmut_11': x_build_sync_plan__mutmut_11, 
    'x_build_sync_plan__mutmut_12': x_build_sync_plan__mutmut_12, 
    'x_build_sync_plan__mutmut_13': x_build_sync_plan__mutmut_13, 
    'x_build_sync_plan__mutmut_14': x_build_sync_plan__mutmut_14, 
    'x_build_sync_plan__mutmut_15': x_build_sync_plan__mutmut_15, 
    'x_build_sync_plan__mutmut_16': x_build_sync_plan__mutmut_16, 
    'x_build_sync_plan__mutmut_17': x_build_sync_plan__mutmut_17, 
    'x_build_sync_plan__mutmut_18': x_build_sync_plan__mutmut_18, 
    'x_build_sync_plan__mutmut_19': x_build_sync_plan__mutmut_19, 
    'x_build_sync_plan__mutmut_20': x_build_sync_plan__mutmut_20, 
    'x_build_sync_plan__mutmut_21': x_build_sync_plan__mutmut_21, 
    'x_build_sync_plan__mutmut_22': x_build_sync_plan__mutmut_22, 
    'x_build_sync_plan__mutmut_23': x_build_sync_plan__mutmut_23, 
    'x_build_sync_plan__mutmut_24': x_build_sync_plan__mutmut_24, 
    'x_build_sync_plan__mutmut_25': x_build_sync_plan__mutmut_25, 
    'x_build_sync_plan__mutmut_26': x_build_sync_plan__mutmut_26
}
x_build_sync_plan__mutmut_orig.__name__ = 'x_build_sync_plan'


def resolve_slug(article_url: str) -> SlugResolution:
    args = [article_url]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_resolve_slug__mutmut_orig, x_resolve_slug__mutmut_mutants, args, kwargs, None)


def x_resolve_slug__mutmut_orig(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, slug=slug)


def x_resolve_slug__mutmut_1(article_url: str) -> SlugResolution:
    try:
        slug = None
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, slug=slug)


def x_resolve_slug__mutmut_2(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(None)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, slug=slug)


def x_resolve_slug__mutmut_3(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=None)

    return ResolvedSlug(article_url=article_url, slug=slug)


def x_resolve_slug__mutmut_4(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=None, slug=slug)


def x_resolve_slug__mutmut_5(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, slug=None)


def x_resolve_slug__mutmut_6(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(slug=slug)


def x_resolve_slug__mutmut_7(article_url: str) -> SlugResolution:
    try:
        slug = Slug.from_article_url(article_url)
    except InvalidArticleUrlError as error:
        return RejectedSlug(reason=f"{article_url}: {error}")

    return ResolvedSlug(article_url=article_url, )

x_resolve_slug__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_resolve_slug__mutmut_1': x_resolve_slug__mutmut_1, 
    'x_resolve_slug__mutmut_2': x_resolve_slug__mutmut_2, 
    'x_resolve_slug__mutmut_3': x_resolve_slug__mutmut_3, 
    'x_resolve_slug__mutmut_4': x_resolve_slug__mutmut_4, 
    'x_resolve_slug__mutmut_5': x_resolve_slug__mutmut_5, 
    'x_resolve_slug__mutmut_6': x_resolve_slug__mutmut_6, 
    'x_resolve_slug__mutmut_7': x_resolve_slug__mutmut_7
}
x_resolve_slug__mutmut_orig.__name__ = 'x_resolve_slug'

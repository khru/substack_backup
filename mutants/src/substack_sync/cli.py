from __future__ import annotations

import argparse
from pathlib import Path

from substack_sync.constants import (
    DEFAULT_FEED_URL,
    DEFAULT_MARKDOWN_ENDPOINT,
    DEFAULT_OUTPUT_DIRECTORY,
    DEFAULT_REQUEST_TIMEOUT_SECONDS,
)
from substack_sync.errors import SubstackSyncError
from substack_sync.http_clients import HttpFeedReader, HttpMarkdownFetcher
from substack_sync.post_repository import FileSystemPostRepository
from substack_sync.use_case import SyncSubstackPostsUseCase

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def main(argv: list[str] | None = None) -> int:
    arguments = _parse_arguments(argv)
    use_case = _build_use_case(arguments)

    return _run_use_case(arguments, use_case)


def _build_use_case(arguments: argparse.Namespace) -> SyncSubstackPostsUseCase:
    return SyncSubstackPostsUseCase(
        feed_reader=HttpFeedReader(timeout_seconds=arguments.timeout_seconds),
        markdown_fetcher=HttpMarkdownFetcher(
            endpoint_url=arguments.markdown_endpoint,
            timeout_seconds=arguments.timeout_seconds,
        ),
        post_repository=FileSystemPostRepository(output_directory=Path(arguments.output_directory)),
    )


def _run_use_case(arguments: argparse.Namespace, use_case: SyncSubstackPostsUseCase) -> int:
    try:
        summary = use_case.sync(feed_url=arguments.feed_url)
    except SubstackSyncError as error:
        print(f"ERROR: {error}")
        return EXIT_FAILURE
    except Exception as error:
        print(f"ERROR: Unexpected failure: {error}")
        return EXIT_FAILURE

    _print_summary(summary.to_log_lines())

    if summary.has_failures:
        _print_summary(tuple(f"ERROR: {failure}" for failure in summary.failures))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def _print_summary(lines: tuple[str, ...]) -> None:
    for line in lines:
        print(line)


def _parse_arguments(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synchronize Substack posts to markdown files in this repository.",
    )
    parser.add_argument(
        "--feed-url",
        default=DEFAULT_FEED_URL,
        help="RSS feed URL to synchronize.",
    )
    parser.add_argument(
        "--markdown-endpoint",
        default=DEFAULT_MARKDOWN_ENDPOINT,
        help="Endpoint prefix used to transform URLs into markdown.",
    )
    parser.add_argument(
        "--output-directory",
        default=DEFAULT_OUTPUT_DIRECTORY,
        help="Directory where markdown files are stored.",
    )
    parser.add_argument(
        "--timeout-seconds",
        default=DEFAULT_REQUEST_TIMEOUT_SECONDS,
        type=int,
        help="HTTP timeout in seconds for feed and markdown requests.",
    )
    return parser.parse_args(argv)

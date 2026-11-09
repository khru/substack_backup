from __future__ import annotations

import argparse
from pathlib import Path

from substack_sync.backup_markdown_images_use_case import BackupMarkdownImagesUseCase
from substack_sync.constants import (
    DEFAULT_IMAGE_BACKUP_DIRECTORY,
    DEFAULT_OUTPUT_DIRECTORY,
    DEFAULT_REQUEST_TIMEOUT_SECONDS,
)
from substack_sync.file_system_image_backup_repository import FileSystemImageBackupRepository
from substack_sync.http_image_fetcher import HttpImageFetcher
from substack_sync.substack_sync_error import SubstackSyncError

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def main(argv: list[str] | None = None) -> int:
    arguments = _parse_arguments(argv)
    use_case = _build_use_case(arguments)

    return _run_use_case(use_case)


def _build_use_case(arguments: argparse.Namespace) -> BackupMarkdownImagesUseCase:
    return BackupMarkdownImagesUseCase(
        posts_directory=Path(arguments.posts_directory),
        image_fetcher=HttpImageFetcher(timeout_seconds=arguments.timeout_seconds),
        image_repository=FileSystemImageBackupRepository(
            output_directory=Path(arguments.images_directory)
        ),
    )


def _run_use_case(use_case: BackupMarkdownImagesUseCase) -> int:
    try:
        summary = use_case.backup()
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
        description="Back up remote images referenced by markdown posts.",
    )
    parser.add_argument(
        "--posts-directory",
        default=DEFAULT_OUTPUT_DIRECTORY,
        help="Directory containing markdown post files.",
    )
    parser.add_argument(
        "--images-directory",
        default=DEFAULT_IMAGE_BACKUP_DIRECTORY,
        help="Directory where downloaded images are stored.",
    )
    parser.add_argument(
        "--timeout-seconds",
        default=DEFAULT_REQUEST_TIMEOUT_SECONDS,
        type=int,
        help="HTTP timeout in seconds for image downloads.",
    )
    return parser.parse_args(argv)

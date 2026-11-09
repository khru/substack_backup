from __future__ import annotations

from pathlib import Path

from substack_sync.image_backup_repository_port import ImageBackupRepository
from substack_sync.image_backup_summary import ImageBackupSummary
from substack_sync.image_fetcher_port import ImageFetcher
from substack_sync.image_url_extractor import extract_remote_image_urls
from substack_sync.substack_sync_error import SubstackSyncError


class BackupMarkdownImagesUseCase:
    def __init__(
        self,
        posts_directory: Path,
        image_fetcher: ImageFetcher,
        image_repository: ImageBackupRepository,
    ) -> None:
        self._posts_directory = posts_directory
        self._image_fetcher = image_fetcher
        self._image_repository = image_repository

    def backup(self) -> ImageBackupSummary:
        markdown_file_paths = self._markdown_file_paths()
        downloaded = 0
        skipped_existing = 0
        images_discovered = 0
        failures: list[str] = []

        for markdown_file_path in markdown_file_paths:
            try:
                markdown_text = markdown_file_path.read_text(encoding="utf-8")
            except OSError as error:
                failures.append(f"{markdown_file_path.name}: {error}")
                continue

            image_urls = extract_remote_image_urls(markdown_text)
            images_discovered += len(image_urls)

            for image_index, image_url in enumerate(image_urls, start=1):
                try:
                    if self._image_repository.has_image(markdown_file_path, image_url, image_index):
                        skipped_existing += 1
                        continue

                    image_content = self._image_fetcher.fetch(image_url)
                    self._image_repository.save_image(
                        markdown_file_path=markdown_file_path,
                        image_url=image_url,
                        image_index=image_index,
                        image_content=image_content,
                    )
                    downloaded += 1
                except SubstackSyncError as error:
                    failures.append(f"{markdown_file_path.name}: {error}")

        return ImageBackupSummary(
            total_posts=len(markdown_file_paths),
            images_discovered=images_discovered,
            downloaded=downloaded,
            skipped_existing=skipped_existing,
            failed=len(failures),
            failures=tuple(failures),
        )

    def _markdown_file_paths(self) -> tuple[Path, ...]:
        if not self._posts_directory.exists():
            return ()

        return tuple(
            sorted(
                post_path for post_path in self._posts_directory.glob("*.md") if post_path.is_file()
            )
        )

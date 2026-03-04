from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

from substack_sync.image_backup_summary import ImageBackupSummary


class ImageBackupCliTests(unittest.TestCase):
    @patch("substack_sync.image_backup_cli.BackupMarkdownImagesUseCase")
    def test_main_returns_failure_when_image_backup_reports_errors(
        self,
        use_case_class: MagicMock,
    ) -> None:
        from substack_sync.image_backup_cli import main

        use_case_instance = use_case_class.return_value
        use_case_instance.backup.return_value = ImageBackupSummary(
            total_posts=1,
            images_discovered=1,
            downloaded=0,
            skipped_existing=0,
            failed=1,
            failures=("post.md: Unable to download image",),
        )

        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(argv=[])

        self.assertEqual(exit_code, 1)
        self.assertIn("Failed downloads: 1", output.getvalue())

    @patch("substack_sync.image_backup_cli.BackupMarkdownImagesUseCase")
    def test_main_returns_success_when_image_backup_is_clean(
        self, use_case_class: MagicMock
    ) -> None:
        from substack_sync.image_backup_cli import main

        use_case_instance = use_case_class.return_value
        use_case_instance.backup.return_value = ImageBackupSummary(
            total_posts=1,
            images_discovered=1,
            downloaded=1,
            skipped_existing=0,
            failed=0,
            failures=(),
        )

        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(argv=[])

        self.assertEqual(exit_code, 0)
        self.assertIn("Downloaded images: 1", output.getvalue())


if __name__ == "__main__":
    unittest.main()

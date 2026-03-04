from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

from substack_sync.models import SyncSummary


class CliTests(unittest.TestCase):
    @patch("substack_sync.cli.SyncSubstackArchivePostsUseCase")
    def test_main_returns_failure_when_summary_has_errors(self, use_case_class: MagicMock) -> None:
        from substack_sync.cli import main

        use_case_instance = use_case_class.return_value
        use_case_instance.sync.return_value = SyncSummary(
            total_urls=1,
            downloaded=0,
            skipped_existing=0,
            failed=1,
            failures=("error",),
        )

        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(argv=[])

        self.assertEqual(exit_code, 1)
        self.assertIn("Failed downloads: 1", output.getvalue())

    @patch("substack_sync.cli.SyncSubstackArchivePostsUseCase")
    def test_main_returns_success_when_sync_is_clean(self, use_case_class: MagicMock) -> None:
        from substack_sync.cli import main

        use_case_instance = use_case_class.return_value
        use_case_instance.sync.return_value = SyncSummary(
            total_urls=1,
            downloaded=1,
            skipped_existing=0,
            failed=0,
            failures=(),
        )

        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(argv=[])

        self.assertEqual(exit_code, 0)

    @patch("substack_sync.cli.SyncSubstackArchivePostsUseCase")
    def test_main_returns_failure_on_unexpected_exception(self, use_case_class: MagicMock) -> None:
        from substack_sync.cli import main

        use_case_instance = use_case_class.return_value
        use_case_instance.sync.side_effect = RuntimeError("boom")

        output = io.StringIO()
        with redirect_stdout(output):
            exit_code = main(argv=[])

        self.assertEqual(exit_code, 1)
        self.assertIn("ERROR: Unexpected failure:", output.getvalue())


if __name__ == "__main__":
    unittest.main()

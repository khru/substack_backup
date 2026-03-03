from __future__ import annotations

import unittest
from pathlib import Path

_FIXTURE_DIRECTORY = Path("tests/fixtures/markdown")
_EXPECTED_FIXTURE_NAMES = (
    "triangulation-in-tdd-and-the-rule.md",
    "testing-actions-calculations-and-data.md",
)


class MarkdownFixtureTests(unittest.TestCase):
    def test_fixtures_exist_and_use_frontmatter_format(self) -> None:
        for fixture_name in _EXPECTED_FIXTURE_NAMES:
            fixture_path = _FIXTURE_DIRECTORY / fixture_name
            self.assertTrue(fixture_path.exists(), msg=f"Missing fixture: {fixture_path}")

            content = fixture_path.read_text(encoding="utf-8")
            self.assertTrue(
                content.startswith("---\n"), msg=f"Invalid frontmatter start: {fixture_path}"
            )
            self.assertIn("\n---\n", content, msg=f"Invalid frontmatter end: {fixture_path}")
            self.assertIn("requested_url:", content, msg=f"Missing requested_url: {fixture_path}")
            self.assertIn("canonical_url:", content, msg=f"Missing canonical_url: {fixture_path}")


if __name__ == "__main__":
    unittest.main()

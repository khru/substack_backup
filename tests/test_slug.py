from __future__ import annotations

import unittest

from substack_sync.errors import InvalidArticleUrlError
from substack_sync.models import Slug


class SlugTests(unittest.TestCase):
    def test_extracts_slug_from_substack_post_url(self) -> None:
        slug = Slug.from_article_url("https://emmanuelvalverderamos.substack.com/p/my-first-post")

        self.assertEqual(slug.value, "my-first-post")

    def test_removes_html_suffix_and_sanitizes_non_ascii_characters(self) -> None:
        slug = Slug.from_article_url(
            "https://emmanuelvalverderamos.substack.com/p/Articulo-con-Acentos-%C3%91andu.html"
        )

        self.assertEqual(slug.value, "articulo-con-acentos-nandu")

    def test_uses_last_segment_for_non_standard_substack_path(self) -> None:
        slug = Slug.from_article_url(
            "https://emmanuelvalverderamos.substack.com/archive/my-special-post"
        )

        self.assertEqual(slug.value, "my-special-post")

    def test_raises_error_when_url_has_no_path_segments(self) -> None:
        with self.assertRaises(InvalidArticleUrlError):
            Slug.from_article_url("https://emmanuelvalverderamos.substack.com")

    def test_file_name_uses_markdown_extension(self) -> None:
        slug = Slug("hello-world")

        self.assertEqual(slug.to_file_name(), "hello-world.md")


if __name__ == "__main__":
    unittest.main()

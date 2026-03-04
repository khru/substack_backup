from __future__ import annotations

import unittest

from substack_sync.archive_parser import ArchivePost, extract_archive_posts
from substack_sync.errors import ArchiveParseError


class ArchiveParserTests(unittest.TestCase):
    def test_extract_archive_posts_returns_timestamped_posts(self) -> None:
        payload = (
            "["
            '{"canonical_url": "https://example.substack.com/p/first-post",'
            '"post_date": "2026-03-03T07:01:06.960Z"},'
            '{"canonical_url": "https://example.substack.com/p/second-post",'
            '"post_date": "2026-03-02T20:10:00.000Z"}'
            "]"
        )

        posts = extract_archive_posts(payload)

        self.assertEqual(
            posts,
            (
                ArchivePost(
                    article_url="https://example.substack.com/p/first-post",
                    published_timestamp="20260303070106",
                ),
                ArchivePost(
                    article_url="https://example.substack.com/p/second-post",
                    published_timestamp="20260302201000",
                ),
            ),
        )

    def test_extract_archive_posts_deduplicates_by_canonical_url(self) -> None:
        payload = (
            "["
            '{"canonical_url": "https://example.substack.com/p/post",'
            '"post_date": "2026-03-03T07:01:06.960Z"},'
            '{"canonical_url": "https://example.substack.com/p/post",'
            '"post_date": "2026-03-03T07:01:06.960Z"}'
            "]"
        )

        posts = extract_archive_posts(payload)

        self.assertEqual(len(posts), 1)

    def test_extract_archive_posts_raises_error_for_invalid_payload(self) -> None:
        with self.assertRaises(ArchiveParseError):
            extract_archive_posts("{}")


if __name__ == "__main__":
    unittest.main()

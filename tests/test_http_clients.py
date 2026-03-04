from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from substack_sync.archive_parser import ArchivePost
from substack_sync.errors import ArchiveDownloadError
from substack_sync.http_clients import HttpArchiveReader


class HttpArchiveReaderTests(unittest.TestCase):
    def test_fetch_reads_archive_pages_using_limit_twenty(self) -> None:
        archive_url = "https://example.workers.dev/archive"
        requested_urls: list[str] = []

        response_by_url = {
            f"{archive_url}?sort=new&search=&offset=0&limit=20": (
                "["
                '{"canonical_url": "https://example.substack.com/p/first", '
                '"post_date": "2026-03-03T07:01:06.960Z"},'
                '{"canonical_url": "https://example.substack.com/p/second", '
                '"post_date": "2026-03-03T06:00:00.000Z"}'
                "]"
            ),
            f"{archive_url}?sort=new&search=&offset=2&limit=20": (
                "["
                '{"canonical_url": "https://example.substack.com/p/third", '
                '"post_date": "2026-03-03T05:00:00.000Z"}'
                "]"
            ),
            f"{archive_url}?sort=new&search=&offset=3&limit=20": "[]",
        }

        def fetch_text(request_url: str) -> str:
            requested_urls.append(request_url)
            return response_by_url[request_url]

        reader = HttpArchiveReader(timeout_seconds=30, fetch_text=fetch_text)

        posts = reader.fetch(archive_url)

        self.assertEqual(
            posts,
            (
                ArchivePost(
                    article_url="https://example.substack.com/p/first",
                    published_timestamp="20260303070106",
                ),
                ArchivePost(
                    article_url="https://example.substack.com/p/second",
                    published_timestamp="20260303060000",
                ),
                ArchivePost(
                    article_url="https://example.substack.com/p/third",
                    published_timestamp="20260303050000",
                ),
            ),
        )
        self.assertEqual(requested_urls, list(response_by_url.keys()))

    def test_fetch_stops_when_first_page_is_empty(self) -> None:
        archive_url = "https://example.workers.dev/archive"

        reader = HttpArchiveReader(timeout_seconds=30, fetch_text=lambda request_url: "[]")

        posts = reader.fetch(archive_url)

        self.assertEqual(posts, ())

    @patch("substack_sync.http_client_helpers.PoolManager")
    def test_fetch_uses_retry_policy_and_raises_for_429_status(
        self, pool_manager_class: MagicMock
    ) -> None:
        pool_manager_instance = pool_manager_class.return_value
        pool_manager_instance.request.return_value = _FakeHttpResponse(status=429, data=b"[]")

        reader = HttpArchiveReader(timeout_seconds=30)

        with self.assertRaises(ArchiveDownloadError):
            reader.fetch("https://example.workers.dev/archive")

        retry_policy = pool_manager_instance.request.call_args.kwargs["retries"]
        self.assertEqual(retry_policy.total, 3)


class _FakeHttpResponse:
    def __init__(self, status: int, data: bytes) -> None:
        self.status = status
        self.data = data


if __name__ == "__main__":
    unittest.main()

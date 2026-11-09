from __future__ import annotations

import unittest
from unittest.mock import patch

from substack_sync.http_markdown_fetcher import HttpMarkdownFetcher
from substack_sync.markdown_download_error import MarkdownDownloadError


class HttpMarkdownFetcherTests(unittest.TestCase):
    @patch("substack_sync.http_markdown_fetcher.fetch_text_response")
    def test_fetch_uses_fallback_when_primary_markdown_endpoint_fails(
        self, fetch_text_response: object
    ) -> None:
        fetch_text_response.side_effect = [  # type: ignore[attr-defined]
            MarkdownDownloadError("primary unavailable"),
            "# Fallback markdown",
        ]
        fetcher = HttpMarkdownFetcher(
            endpoint_url="https://primary.example/?url=",
            fallback_endpoint_url="https://r.jina.ai/http://",
            timeout_seconds=30,
        )

        markdown = fetcher.fetch("https://example.substack.com/p/post")

        self.assertEqual(markdown, "# Fallback markdown")
        self.assertEqual(fetch_text_response.call_count, 2)  # type: ignore[attr-defined]
        fallback_url = fetch_text_response.call_args_list[1].kwargs["target_url"]  # type: ignore[attr-defined]
        self.assertEqual(fallback_url, "https://r.jina.ai/http://example.substack.com/p/post")


if __name__ == "__main__":
    unittest.main()

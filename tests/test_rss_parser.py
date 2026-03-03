from __future__ import annotations

import unittest

from substack_sync.errors import RssParseError
from substack_sync.rss_parser import extract_article_urls

_RSS_TEMPLATE = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<rss version=\"2.0\">
  <channel>
    <title>Example Feed</title>
    <item>
      <link>https://emmanuelvalverderamos.substack.com/p/post-one</link>
    </item>
    <item>
      <link>https://emmanuelvalverderamos.substack.com/p/post-two</link>
    </item>
    <item>
      <link>https://emmanuelvalverderamos.substack.com/p/post-one</link>
    </item>
    <item>
      <link>mailto:hello@example.com</link>
    </item>
  </channel>
</rss>
"""

_ATOM_TEMPLATE = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<feed xmlns=\"http://www.w3.org/2005/Atom\">
  <title>Example Atom</title>
  <entry>
    <link href=\"https://emmanuelvalverderamos.substack.com/p/atom-one\" rel=\"alternate\" />
  </entry>
  <entry>
    <link href=\"https://emmanuelvalverderamos.substack.com/p/atom-two\" rel=\"alternate\" />
  </entry>
</feed>
"""


class RssParserTests(unittest.TestCase):
    def test_extracts_unique_http_urls_from_rss_feed(self) -> None:
        urls = extract_article_urls(_RSS_TEMPLATE)

        self.assertEqual(
            urls,
            [
                "https://emmanuelvalverderamos.substack.com/p/post-one",
                "https://emmanuelvalverderamos.substack.com/p/post-two",
            ],
        )

    def test_extracts_links_from_atom_feed(self) -> None:
        urls = extract_article_urls(_ATOM_TEMPLATE)

        self.assertEqual(
            urls,
            [
                "https://emmanuelvalverderamos.substack.com/p/atom-one",
                "https://emmanuelvalverderamos.substack.com/p/atom-two",
            ],
        )

    def test_raises_error_for_invalid_xml(self) -> None:
        with self.assertRaises(RssParseError):
            extract_article_urls("<rss>")

    def test_raises_error_for_empty_content(self) -> None:
        with self.assertRaises(RssParseError):
            extract_article_urls("   ")


if __name__ == "__main__":
    unittest.main()

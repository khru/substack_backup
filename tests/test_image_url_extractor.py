from __future__ import annotations

import unittest

from substack_sync.image_url_extractor import extract_remote_image_urls


class ImageUrlExtractorTests(unittest.TestCase):
    def test_extract_remote_image_urls_supports_markdown_and_html_images(self) -> None:
        markdown_text = """
        Intro
        ![Cover](https://example.com/cover.png)
        [![](https://example.com/diagram.jpeg)](https://example.com/post)
        <img src="https://images.example.com/banner.webp" alt="banner" />
        ![Duplicate](https://example.com/cover.png)
        """

        image_urls = extract_remote_image_urls(markdown_text)

        self.assertEqual(
            image_urls,
            (
                "https://example.com/cover.png",
                "https://example.com/diagram.jpeg",
                "https://images.example.com/banner.webp",
            ),
        )

    def test_extract_remote_image_urls_ignores_non_http_schemes_and_missing_images(self) -> None:
        markdown_text = """
        No remote images.
        ![local](./image.png)
        ![inline](data:image/png;base64,abc)
        <img src="mailto:hello@example.com" />
        """

        image_urls = extract_remote_image_urls(markdown_text)

        self.assertEqual(image_urls, ())


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import re
from urllib.parse import urlparse

MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\((?P<url>[^)\s]+)")
HTML_IMAGE_PATTERN = re.compile(r"<img\b[^>]*\bsrc=[\"'](?P<url>[^\"']+)[\"']", re.IGNORECASE)


def extract_remote_image_urls(markdown_text: str) -> tuple[str, ...]:
    discovered_urls: list[str] = []
    seen_urls: set[str] = set()

    for image_url in _extract_candidate_urls(markdown_text):
        parsed_url = urlparse(image_url)
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            continue

        if image_url in seen_urls:
            continue

        seen_urls.add(image_url)
        discovered_urls.append(image_url)

    return tuple(discovered_urls)


def _extract_candidate_urls(markdown_text: str) -> tuple[str, ...]:
    markdown_matches = tuple(
        match.group("url") for match in MARKDOWN_IMAGE_PATTERN.finditer(markdown_text)
    )
    html_matches = tuple(match.group("url") for match in HTML_IMAGE_PATTERN.finditer(markdown_text))
    return (*markdown_matches, *html_matches)

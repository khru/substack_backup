from __future__ import annotations

from urllib.parse import urlparse
from xml.etree import ElementTree

from substack_sync.constants import (
    ATOM_ENTRY_TAG,
    ATOM_HREF_ATTRIBUTE,
    ATOM_LINK_TAG,
    RSS_ITEM_TAG,
    RSS_LINK_TAG,
)
from substack_sync.errors import RssParseError


def extract_article_urls(feed_xml: str) -> list[str]:
    if not feed_xml.strip():
        raise RssParseError("RSS feed content is empty.")

    try:
        root = ElementTree.fromstring(feed_xml)
    except ElementTree.ParseError as error:
        raise RssParseError("RSS feed XML is invalid.") from error

    links = _extract_rss_item_links(root)
    links.extend(_extract_atom_entry_links(root))
    return _deduplicate_http_urls(links)


def _extract_rss_item_links(root: ElementTree.Element) -> list[str]:
    links: list[str] = []
    for item in root.iter():
        if _local_name(item.tag) != RSS_ITEM_TAG:
            continue

        for child in item:
            if _local_name(child.tag) != RSS_LINK_TAG:
                continue

            if child.text is None:
                continue

            links.append(child.text.strip())
            break

    return links


def _extract_atom_entry_links(root: ElementTree.Element) -> list[str]:
    links: list[str] = []
    for entry in root.iter():
        if _local_name(entry.tag) != ATOM_ENTRY_TAG:
            continue

        for child in entry:
            if _local_name(child.tag) != ATOM_LINK_TAG:
                continue

            href = child.attrib.get(ATOM_HREF_ATTRIBUTE, "").strip()
            if href:
                links.append(href)
                break

    return links


def _deduplicate_http_urls(urls: list[str]) -> list[str]:
    deduplicated_urls: list[str] = []
    seen_urls: set[str] = set()

    for url in urls:
        candidate_url = url.strip()
        if not candidate_url:
            continue

        parsed = urlparse(candidate_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            continue

        if candidate_url in seen_urls:
            continue

        seen_urls.add(candidate_url)
        deduplicated_urls.append(candidate_url)

    return deduplicated_urls


def _local_name(tag: str) -> str:
    if "}" not in tag:
        return tag

    return tag.split("}", maxsplit=1)[1]

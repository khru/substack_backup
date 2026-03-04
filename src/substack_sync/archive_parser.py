from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime

from substack_sync.errors import ArchiveParseError


@dataclass(frozen=True)
class ArchivePost:
    article_url: str
    published_timestamp: str


def extract_archive_posts(archive_payload: str) -> tuple[ArchivePost, ...]:
    if not archive_payload.strip():
        raise ArchiveParseError("Archive payload is empty.")

    try:
        raw_items = json.loads(archive_payload)
    except json.JSONDecodeError as error:
        raise ArchiveParseError("Archive payload is not valid JSON.") from error

    if not isinstance(raw_items, list):
        raise ArchiveParseError("Archive payload must be a JSON array.")

    posts: list[ArchivePost] = []
    seen_urls: set[str] = set()
    for raw_item in raw_items:
        post = _parse_post(raw_item)
        if post.article_url in seen_urls:
            continue

        seen_urls.add(post.article_url)
        posts.append(post)

    return tuple(posts)


def _parse_post(raw_item: object) -> ArchivePost:
    if not isinstance(raw_item, dict):
        raise ArchiveParseError("Archive items must be JSON objects.")

    article_url = raw_item.get("canonical_url")
    post_date = raw_item.get("post_date")
    if not isinstance(article_url, str) or not article_url.strip():
        raise ArchiveParseError("Archive item is missing canonical_url.")
    if not isinstance(post_date, str) or not post_date.strip():
        raise ArchiveParseError("Archive item is missing post_date.")

    published_timestamp = _to_timestamp(post_date)
    return ArchivePost(article_url=article_url.strip(), published_timestamp=published_timestamp)


def _to_timestamp(post_date: str) -> str:
    try:
        date_time = datetime.fromisoformat(post_date.replace("Z", "+00:00"))
    except ValueError as error:
        raise ArchiveParseError(f"Archive post_date is invalid: {post_date}") from error

    if date_time.tzinfo is None:
        date_time = date_time.replace(tzinfo=UTC)
    else:
        date_time = date_time.astimezone(UTC)

    return date_time.strftime("%Y%m%d%H%M%S")

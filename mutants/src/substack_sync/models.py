from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from urllib.parse import unquote, urlparse

from substack_sync.constants import HTML_EXTENSION, MARKDOWN_EXTENSION, SUBSTACK_POST_PREFIX
from substack_sync.errors import EmptyMarkdownError, InvalidArticleUrlError

_NON_SLUG_CHARACTER_PATTERN = re.compile(r"[^a-z0-9-]+")
_MULTIPLE_DASH_PATTERN = re.compile(r"-{2,}")


@dataclass(frozen=True)
class Slug:
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise InvalidArticleUrlError("Slug cannot be empty.")

    @classmethod
    def from_article_url(cls, article_url: str) -> Slug:
        parsed_url = urlparse(article_url)
        if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
            raise InvalidArticleUrlError(f"Invalid article URL: {article_url}")

        path_segments = [segment for segment in parsed_url.path.split("/") if segment]
        if not path_segments:
            raise InvalidArticleUrlError(f"Article URL has no path segments: {article_url}")

        slug_candidate = path_segments[-1]
        if len(path_segments) >= 2 and path_segments[0] == SUBSTACK_POST_PREFIX:
            slug_candidate = path_segments[1]

        slug_candidate = unquote(slug_candidate)
        slug_candidate = slug_candidate.removesuffix(HTML_EXTENSION)

        normalized_candidate = unicodedata.normalize("NFKD", slug_candidate)
        ascii_candidate = normalized_candidate.encode("ascii", "ignore").decode("ascii").lower()
        sanitized_slug = _NON_SLUG_CHARACTER_PATTERN.sub("-", ascii_candidate)
        sanitized_slug = _MULTIPLE_DASH_PATTERN.sub("-", sanitized_slug).strip("-")

        if not sanitized_slug:
            raise InvalidArticleUrlError(f"Article URL has no valid slug content: {article_url}")

        return cls(sanitized_slug)

    def to_file_name(self) -> str:
        return f"{self.value}{MARKDOWN_EXTENSION}"


@dataclass(frozen=True)
class MarkdownDocument:
    content: str

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise EmptyMarkdownError("Markdown content is empty.")

    @classmethod
    def from_raw_text(cls, raw_markdown: str) -> MarkdownDocument:
        normalized_markdown = raw_markdown if raw_markdown.endswith("\n") else f"{raw_markdown}\n"
        return cls(content=normalized_markdown)


@dataclass(frozen=True)
class SyncSummary:
    total_urls: int
    downloaded: int
    skipped_existing: int
    failed: int
    failures: tuple[str, ...]

    @property
    def has_failures(self) -> bool:
        return self.failed > 0

    def to_log_lines(self) -> tuple[str, ...]:
        return (
            f"Total feed URLs: {self.total_urls}",
            f"Downloaded posts: {self.downloaded}",
            f"Skipped existing posts: {self.skipped_existing}",
            f"Failed downloads: {self.failed}",
        )

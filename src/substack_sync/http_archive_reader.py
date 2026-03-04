from __future__ import annotations

from collections.abc import Callable

from substack_sync.archive_download_error import ArchiveDownloadError
from substack_sync.archive_parser import ArchivePost, extract_archive_posts
from substack_sync.constants import (
    DEFAULT_ARCHIVE_PAGE_LIMIT,
    DEFAULT_HTTP_MAX_RETRIES,
    DEFAULT_HTTP_USER_AGENT,
)
from substack_sync.http_client_helpers import (
    build_archive_request_url,
    fetch_text_response,
    resolve_circuit_breaker,
)
from substack_sync.resilience import CircuitBreakerPort


class HttpArchiveReader:
    def __init__(
        self,
        timeout_seconds: int,
        page_limit: int = DEFAULT_ARCHIVE_PAGE_LIMIT,
        user_agent: str = DEFAULT_HTTP_USER_AGENT,
        fetch_text: Callable[[str], str] | None = None,
        max_retries: int = DEFAULT_HTTP_MAX_RETRIES,
        circuit_breaker: CircuitBreakerPort | None = None,
    ) -> None:
        self._timeout_seconds = timeout_seconds
        self._page_limit = page_limit
        self._user_agent = user_agent
        self._fetch_text = fetch_text
        self._max_retries = max_retries
        self._circuit_breaker = resolve_circuit_breaker(circuit_breaker)

    def fetch(self, archive_url: str) -> tuple[ArchivePost, ...]:
        posts: list[ArchivePost] = []
        offset = 0

        while True:
            request_url = build_archive_request_url(
                archive_url=archive_url,
                offset=offset,
                limit=self._page_limit,
            )
            page_payload = self._fetch_page_payload(request_url)
            page_posts = extract_archive_posts(page_payload)

            if not page_posts:
                break

            posts.extend(page_posts)
            offset += len(page_posts)

        return tuple(posts)

    def _fetch_page_payload(self, request_url: str) -> str:
        if self._fetch_text is not None:
            return self._fetch_text(request_url)

        return fetch_text_response(
            target_url=request_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=ArchiveDownloadError,
            operation_label="archive page",
            max_retries=self._max_retries,
            circuit_breaker=self._circuit_breaker,
        )

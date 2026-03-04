from __future__ import annotations

from collections.abc import Callable
from urllib.parse import quote, urlencode

from urllib3 import PoolManager
from urllib3.exceptions import HTTPError as UrlLib3HttpError

from substack_sync.archive_parser import ArchivePost, extract_archive_posts
from substack_sync.constants import (
    DEFAULT_ARCHIVE_PAGE_LIMIT,
    DEFAULT_ARCHIVE_SEARCH,
    DEFAULT_ARCHIVE_SORT,
    DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
    DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
    DEFAULT_HTTP_MAX_RETRIES,
    DEFAULT_HTTP_USER_AGENT,
    HTTP_STATUS_OK,
)
from substack_sync.errors import ArchiveDownloadError, FeedDownloadError, MarkdownDownloadError
from substack_sync.resilience import CircuitBreakerPort, build_circuit_breaker, build_retry_policy


class HttpFeedReader:
    def __init__(
        self,
        timeout_seconds: int,
        user_agent: str = DEFAULT_HTTP_USER_AGENT,
        max_retries: int = DEFAULT_HTTP_MAX_RETRIES,
        circuit_breaker: CircuitBreakerPort | None = None,
    ) -> None:
        self._timeout_seconds = timeout_seconds
        self._user_agent = user_agent
        self._max_retries = max_retries
        self._circuit_breaker = _resolve_circuit_breaker(circuit_breaker)

    def fetch(self, feed_url: str) -> str:
        return _fetch_text_response(
            target_url=feed_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=FeedDownloadError,
            operation_label="RSS feed",
            max_retries=self._max_retries,
            circuit_breaker=self._circuit_breaker,
        )


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
        self._circuit_breaker = _resolve_circuit_breaker(circuit_breaker)

    def fetch(self, archive_url: str) -> tuple[ArchivePost, ...]:
        posts: list[ArchivePost] = []
        offset = 0

        while True:
            request_url = _build_archive_request_url(
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

        return _fetch_text_response(
            target_url=request_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=ArchiveDownloadError,
            operation_label="archive page",
            max_retries=self._max_retries,
            circuit_breaker=self._circuit_breaker,
        )


class HttpMarkdownFetcher:
    def __init__(
        self,
        endpoint_url: str,
        timeout_seconds: int,
        user_agent: str = DEFAULT_HTTP_USER_AGENT,
        max_retries: int = DEFAULT_HTTP_MAX_RETRIES,
        circuit_breaker: CircuitBreakerPort | None = None,
    ) -> None:
        self._endpoint_url = endpoint_url
        self._timeout_seconds = timeout_seconds
        self._user_agent = user_agent
        self._max_retries = max_retries
        self._circuit_breaker = _resolve_circuit_breaker(circuit_breaker)

    def fetch(self, article_url: str) -> str:
        encoded_article_url = quote(article_url, safe="")
        request_url = f"{self._endpoint_url}{encoded_article_url}"
        return _fetch_text_response(
            target_url=request_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=MarkdownDownloadError,
            operation_label="markdown",
            max_retries=self._max_retries,
            circuit_breaker=self._circuit_breaker,
        )


def _fetch_text_response(
    target_url: str,
    timeout_seconds: int,
    user_agent: str,
    error_type: type[Exception],
    operation_label: str,
    max_retries: int,
    circuit_breaker: CircuitBreakerPort,
) -> str:
    retry_policy = build_retry_policy(max_retries=max_retries)
    http_client = PoolManager()

    try:
        response = circuit_breaker.call(
            lambda: http_client.request(
                method="GET",
                url=target_url,
                headers={"User-Agent": user_agent},
                timeout=timeout_seconds,
                retries=retry_policy,
            )
        )
        status_code = int(response.status)
        body = response.data.decode("utf-8")
    except (UrlLib3HttpError, UnicodeDecodeError, ValueError) as error:
        raise error_type(f"Unable to download {operation_label} from {target_url}") from error

    if status_code != HTTP_STATUS_OK:
        raise error_type(
            f"Unable to download {operation_label} from {target_url}: HTTP {status_code}"
        )

    return body


def _build_archive_request_url(archive_url: str, offset: int, limit: int) -> str:
    query = urlencode(
        {
            "sort": DEFAULT_ARCHIVE_SORT,
            "search": DEFAULT_ARCHIVE_SEARCH,
            "offset": offset,
            "limit": limit,
        }
    )
    separator = "&" if "?" in archive_url else "?"
    return f"{archive_url}{separator}{query}"


def _resolve_circuit_breaker(circuit_breaker: CircuitBreakerPort | None) -> CircuitBreakerPort:
    if circuit_breaker is not None:
        return circuit_breaker

    return build_circuit_breaker(
        fail_max=DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
        reset_timeout_seconds=DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
    )

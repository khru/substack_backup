from __future__ import annotations

from urllib.parse import quote

from substack_sync.constants import DEFAULT_HTTP_MAX_RETRIES, DEFAULT_HTTP_USER_AGENT
from substack_sync.http_client_helpers import fetch_text_response, resolve_circuit_breaker
from substack_sync.markdown_download_error import MarkdownDownloadError
from substack_sync.resilience import CircuitBreakerPort


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
        self._circuit_breaker = resolve_circuit_breaker(circuit_breaker)

    def fetch(self, article_url: str) -> str:
        encoded_article_url = quote(article_url, safe="")
        request_url = f"{self._endpoint_url}{encoded_article_url}"
        return fetch_text_response(
            target_url=request_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=MarkdownDownloadError,
            operation_label="markdown",
            max_retries=self._max_retries,
            circuit_breaker=self._circuit_breaker,
        )

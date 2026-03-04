from __future__ import annotations

from urllib3 import PoolManager
from urllib3.exceptions import HTTPError as UrlLib3HttpError

from substack_sync.circuit_breaker_port import CircuitBreakerPort
from substack_sync.constants import (
    DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
    DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
    DEFAULT_HTTP_MAX_RETRIES,
    DEFAULT_HTTP_USER_AGENT,
    HTTP_STATUS_OK,
)
from substack_sync.image_download_error import ImageDownloadError
from substack_sync.resilience import build_circuit_breaker, build_retry_policy


class HttpImageFetcher:
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
        self._circuit_breaker = (
            circuit_breaker
            if circuit_breaker is not None
            else build_circuit_breaker(
                fail_max=DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
                reset_timeout_seconds=DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
            )
        )

    def fetch(self, image_url: str) -> bytes:
        retry_policy = build_retry_policy(max_retries=self._max_retries)
        http_client = PoolManager()

        try:
            response = self._circuit_breaker.call(
                lambda: http_client.request(
                    method="GET",
                    url=image_url,
                    headers={"User-Agent": self._user_agent},
                    timeout=self._timeout_seconds,
                    retries=retry_policy,
                )
            )
            status_code = int(response.status)
            body = bytes(response.data)
        except (UrlLib3HttpError, ValueError) as error:
            raise ImageDownloadError(f"Unable to download image from {image_url}") from error

        if status_code != HTTP_STATUS_OK:
            raise ImageDownloadError(
                f"Unable to download image from {image_url}: HTTP {status_code}"
            )

        if not body:
            raise ImageDownloadError(f"Unable to download image from {image_url}: empty response")

        return body

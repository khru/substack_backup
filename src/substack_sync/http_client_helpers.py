from __future__ import annotations

from urllib.parse import urlencode

from urllib3 import PoolManager
from urllib3.exceptions import HTTPError as UrlLib3HttpError

from substack_sync.constants import (
    DEFAULT_ARCHIVE_SEARCH,
    DEFAULT_ARCHIVE_SORT,
    DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
    DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
    HTTP_STATUS_OK,
)
from substack_sync.resilience import CircuitBreakerPort, build_circuit_breaker, build_retry_policy


def fetch_text_response(
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


def build_archive_request_url(archive_url: str, offset: int, limit: int) -> str:
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


def resolve_circuit_breaker(circuit_breaker: CircuitBreakerPort | None) -> CircuitBreakerPort:
    if circuit_breaker is not None:
        return circuit_breaker

    return build_circuit_breaker(
        fail_max=DEFAULT_CIRCUIT_BREAKER_FAIL_MAX,
        reset_timeout_seconds=DEFAULT_CIRCUIT_BREAKER_RESET_TIMEOUT_SECONDS,
    )

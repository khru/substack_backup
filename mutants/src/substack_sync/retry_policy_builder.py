from __future__ import annotations

from urllib3.util.retry import Retry

RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)


def build_retry_policy(max_retries: int) -> Retry:
    return Retry(
        total=max_retries,
        connect=max_retries,
        read=max_retries,
        status=max_retries,
        backoff_factor=0.5,
        status_forcelist=RETRYABLE_STATUS_CODES,
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )

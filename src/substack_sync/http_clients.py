from __future__ import annotations

from typing import cast
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from substack_sync.constants import DEFAULT_HTTP_USER_AGENT, HTTP_STATUS_OK
from substack_sync.errors import FeedDownloadError, MarkdownDownloadError


class HttpFeedReader:
    def __init__(self, timeout_seconds: int, user_agent: str = DEFAULT_HTTP_USER_AGENT) -> None:
        self._timeout_seconds = timeout_seconds
        self._user_agent = user_agent

    def fetch(self, feed_url: str) -> str:
        return _fetch_text_response(
            target_url=feed_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=FeedDownloadError,
            operation_label="RSS feed",
        )


class HttpMarkdownFetcher:
    def __init__(
        self, endpoint_url: str, timeout_seconds: int, user_agent: str = DEFAULT_HTTP_USER_AGENT
    ) -> None:
        self._endpoint_url = endpoint_url
        self._timeout_seconds = timeout_seconds
        self._user_agent = user_agent

    def fetch(self, article_url: str) -> str:
        encoded_article_url = quote(article_url, safe="")
        request_url = f"{self._endpoint_url}{encoded_article_url}"
        return _fetch_text_response(
            target_url=request_url,
            timeout_seconds=self._timeout_seconds,
            user_agent=self._user_agent,
            error_type=MarkdownDownloadError,
            operation_label="markdown",
        )


def _fetch_text_response(
    target_url: str,
    timeout_seconds: int,
    user_agent: str,
    error_type: type[Exception],
    operation_label: str,
) -> str:
    request = Request(target_url, headers={"User-Agent": user_agent})

    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            status_code = int(getattr(response, "status", HTTP_STATUS_OK))
            response_bytes = cast(bytes, response.read())
            body = response_bytes.decode("utf-8")
    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        raise error_type(f"Unable to download {operation_label} from {target_url}") from error

    if status_code != HTTP_STATUS_OK:
        raise error_type(
            f"Unable to download {operation_label} from {target_url}: HTTP {status_code}"
        )

    return body

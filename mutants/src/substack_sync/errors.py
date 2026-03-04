class SubstackSyncError(Exception):
    """Base exception for sync failures."""


class FeedDownloadError(SubstackSyncError):
    """Raised when RSS feed download fails."""


class ArchiveDownloadError(SubstackSyncError):
    """Raised when archive API download fails."""


class RssParseError(SubstackSyncError):
    """Raised when RSS content cannot be parsed."""


class ArchiveParseError(SubstackSyncError):
    """Raised when archive content cannot be parsed."""


class InvalidArticleUrlError(SubstackSyncError):
    """Raised when article URL cannot produce a safe slug."""


class MarkdownDownloadError(SubstackSyncError):
    """Raised when markdown endpoint request fails."""


class EmptyMarkdownError(SubstackSyncError):
    """Raised when markdown content is empty after download."""


class PostPersistenceError(SubstackSyncError):
    """Raised when markdown cannot be written to disk."""


class CircuitBreakerOpenError(SubstackSyncError):
    """Raised when a circuit breaker is open and short-circuits a call."""

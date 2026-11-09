from substack_sync.substack_sync_error import SubstackSyncError


class InvalidArticleUrlError(SubstackSyncError):
    """Raised when article URL cannot produce a safe slug."""

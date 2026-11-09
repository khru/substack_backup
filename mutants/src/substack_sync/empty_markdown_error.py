from substack_sync.substack_sync_error import SubstackSyncError


class EmptyMarkdownError(SubstackSyncError):
    """Raised when markdown content is empty after download."""

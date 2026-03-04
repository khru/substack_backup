from substack_sync.substack_sync_error import SubstackSyncError


class RssParseError(SubstackSyncError):
    """Raised when RSS content cannot be parsed."""

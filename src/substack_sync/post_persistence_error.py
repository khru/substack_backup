from substack_sync.substack_sync_error import SubstackSyncError


class PostPersistenceError(SubstackSyncError):
    """Raised when markdown cannot be written to disk."""

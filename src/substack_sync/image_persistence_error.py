from substack_sync.substack_sync_error import SubstackSyncError


class ImagePersistenceError(SubstackSyncError):
    """Raised when image cannot be written to disk."""

from substack_sync.substack_sync_error import SubstackSyncError


class ArchiveDownloadError(SubstackSyncError):
    """Raised when archive API download fails."""

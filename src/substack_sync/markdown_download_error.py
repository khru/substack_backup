from substack_sync.substack_sync_error import SubstackSyncError


class MarkdownDownloadError(SubstackSyncError):
    """Raised when markdown endpoint request fails."""

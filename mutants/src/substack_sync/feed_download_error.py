from substack_sync.substack_sync_error import SubstackSyncError


class FeedDownloadError(SubstackSyncError):
    """Raised when RSS feed download fails."""

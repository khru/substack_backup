from substack_sync.substack_sync_error import SubstackSyncError


class ArchiveParseError(SubstackSyncError):
    """Raised when archive content cannot be parsed."""

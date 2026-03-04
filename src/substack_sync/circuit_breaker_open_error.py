from substack_sync.substack_sync_error import SubstackSyncError


class CircuitBreakerOpenError(SubstackSyncError):
    """Raised when a circuit breaker is open and short-circuits a call."""

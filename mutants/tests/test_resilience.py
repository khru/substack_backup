from __future__ import annotations

import unittest

from substack_sync.errors import CircuitBreakerOpenError
from substack_sync.resilience import NullCircuitBreaker, build_circuit_breaker, build_retry_policy


class ResilienceTests(unittest.TestCase):
    def test_build_retry_policy_retries_too_many_requests_three_times(self) -> None:
        retry_policy = build_retry_policy(max_retries=3)

        self.assertEqual(retry_policy.total, 3)
        self.assertIn(429, retry_policy.status_forcelist)
        self.assertTrue(retry_policy.respect_retry_after_header)

    def test_build_retry_policy_retries_transient_server_errors(self) -> None:
        retry_policy = build_retry_policy(max_retries=3)

        self.assertIn(500, retry_policy.status_forcelist)
        self.assertIn(502, retry_policy.status_forcelist)
        self.assertIn(503, retry_policy.status_forcelist)
        self.assertIn(504, retry_policy.status_forcelist)

    def test_null_circuit_breaker_executes_operation(self) -> None:
        circuit_breaker = NullCircuitBreaker()

        result = circuit_breaker.call(lambda: "ok")

        self.assertEqual(result, "ok")

    def test_circuit_breaker_opens_after_failure_threshold(self) -> None:
        circuit_breaker = build_circuit_breaker(fail_max=1, reset_timeout_seconds=60)

        with self.assertRaises(CircuitBreakerOpenError):
            circuit_breaker.call(_always_fail)

        with self.assertRaises(CircuitBreakerOpenError):
            circuit_breaker.call(lambda: "should not run")


def _always_fail() -> str:
    raise RuntimeError("boom")


if __name__ == "__main__":
    unittest.main()

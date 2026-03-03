from __future__ import annotations

import unittest

from substack_sync.models import Slug
from substack_sync.sync_planning import DownloadCandidate, SyncPlan, build_sync_plan


class SyncPlanningTests(unittest.TestCase):
    def test_build_sync_plan_splits_new_existing_and_invalid_urls(self) -> None:
        article_urls = [
            "https://emmanuelvalverderamos.substack.com/p/already-saved",
            "https://emmanuelvalverderamos.substack.com/p/new-post",
            "https://emmanuelvalverderamos.substack.com/",
        ]

        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=frozenset({"already-saved"}),
        )

        self.assertEqual(
            plan,
            SyncPlan(
                download_candidates=(
                    DownloadCandidate(
                        article_url="https://emmanuelvalverderamos.substack.com/p/new-post",
                        slug=Slug("new-post"),
                    ),
                ),
                skipped_existing=1,
                rejected_urls=(
                    "https://emmanuelvalverderamos.substack.com/: "
                    "Article URL has no path segments: "
                    "https://emmanuelvalverderamos.substack.com/",
                ),
            ),
        )

    def test_build_sync_plan_continues_after_rejected_url(self) -> None:
        article_urls = [
            "https://emmanuelvalverderamos.substack.com/",
            "https://emmanuelvalverderamos.substack.com/p/new-post",
        ]

        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=frozenset(),
        )

        self.assertEqual(
            plan.download_candidates,
            (
                DownloadCandidate(
                    article_url="https://emmanuelvalverderamos.substack.com/p/new-post",
                    slug=Slug("new-post"),
                ),
            ),
        )

    def test_build_sync_plan_counts_all_existing_urls(self) -> None:
        article_urls = [
            "https://emmanuelvalverderamos.substack.com/p/already-saved-1",
            "https://emmanuelvalverderamos.substack.com/p/already-saved-2",
        ]

        plan = build_sync_plan(
            article_urls=article_urls,
            existing_slug_values=frozenset({"already-saved-1", "already-saved-2"}),
        )

        self.assertEqual(plan.skipped_existing, 2)


if __name__ == "__main__":
    unittest.main()

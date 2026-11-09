from __future__ import annotations

from dataclasses import dataclass

from substack_sync.models import Slug


@dataclass(frozen=True)
class ResolvedSlug:
    article_url: str
    slug: Slug

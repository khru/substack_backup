# ADR-0003: Archive API pagination and timestamped markdown filenames

- Status: accepted
- Date: 2026-03-04
- Deciders: repository maintainers

## Context

RSS feeds and direct endpoints may expose only recent posts. The project needs complete historical synchronization, idempotent updates, and deterministic file ordering.

## Decision

- Use archive API pagination through a Cloudflare worker proxy.
- Use default archive page size `limit=20` and advance offset using observed page size.
- Persist posts as `posts/<YYYYMMDDHHMMSS>-<slug>.md` in UTC.
- Compare markdown MD5 hashes to decide unchanged vs update behavior.
- Migrate legacy `posts/<slug>.md` files without creating duplicates.

## Consequences

### Positive

- Full historical synchronization is supported.
- File names sort by publication timestamp.
- Updated articles can be re-synced without losing history in git.

### Negative

- Repository logic is more complex due to migration and deduplication paths.

### Follow-up actions

- Maintain focused tests for timestamp parsing, deduplication, and hash-based updates.

# ADR-0004: Independent image backup workflow with per-post asset directories

- Status: accepted
- Date: 2026-03-04
- Deciders: repository maintainers

## Context

Markdown posts include remote image URLs hosted outside this repository. The project needs local image backups to reduce dependency on external availability while keeping markdown synchronization and image backup concerns decoupled.

## Decision

- Add a dedicated image backup process independent from article synchronization.
- Process all `posts/*.md` files and download referenced remote images.
- Store images under `img/<markdown_stem>/` where `<markdown_stem>` includes timestamp and slug.
- Keep markdown files unchanged; image backup must not rewrite markdown links.
- Fail the image backup process if any required image cannot be downloaded.
- Run image backup in a dedicated GitHub Actions workflow with separate triggers and commit path.

## Consequences

### Positive

- Image backup failure does not block article synchronization execution.
- Alerting is explicit when image downloads fail.
- Asset layout remains deterministic and easy to inspect.

### Negative

- Synchronization and image backup are eventually consistent rather than atomic.
- Additional workflow and repository storage growth must be maintained.

### Follow-up actions

- Keep tests for URL extraction, idempotency, and failure signaling.
- Keep README and AGENTS aligned with image backup invariants.

# Live Test List

This file is the execution source of truth for TDD order.

## Status values

- `pending`
- `in_progress`
- `done`
- `blocked`

## Backlog

| ID | Priority | Status | ZOMBIES | Case type | Description | Related commit hash |
| --- | --- | --- | --- | --- | --- | --- |
| GOV-001 | high | done | S | on-point | Enforce "one focused failing test per Red step" in AGENTS | - |
| GOV-002 | high | done | S | on-point | Enforce "run smallest relevant tests after each production change" in AGENTS | - |
| GOV-003 | high | done | S | on-point | Enforce mandatory mutation gate before next test | - |
| GOV-004 | high | done | I | on-point | Enforce live test list protocol in AGENTS | - |
| GOV-005 | high | done | I | on-point | Enforce ADR-first protocol in AGENTS | - |
| GOV-006 | high | done | I | on-point | Enforce ports/adapters architecture rules in AGENTS | - |
| GOV-007 | high | done | I | on-point | Enforce null object and immutability defaults in AGENTS | - |
| GOV-008 | high | done | I | on-point | Enforce FIRST principles and test desiderata in AGENTS | - |
| GOV-009 | high | done | I | on-point | Enforce complete test smells catalog in AGENTS | - |
| GOV-010 | high | done | I | on-point | Enforce complete code smell catalog and parallel change recipes in AGENTS | - |
| DOC-001 | high | done | I | on-point | README explains project purpose and problem solved | - |
| DOC-002 | high | done | I | on-point | README documents stack, setup, and usage commands | - |
| DOC-003 | high | done | I | on-point | README links to ADR directory and decisions | - |
| DOC-004 | medium | done | I | on-point | README documents resilience libraries and rationale | - |
| DOC-005 | medium | done | I | on-point | README and AGENTS maintenance workflow remains explicit | - |
| ADR-001 | high | done | I | on-point | ADR template exists with required sections | - |
| ADR-002 | high | done | I | on-point | Ports and adapters decision is recorded | - |
| ADR-003 | high | done | I | on-point | Quality gate and mutation scope decision is recorded | - |
| ADR-004 | high | done | I | on-point | Archive API + timestamp naming + md5 decision is recorded | - |
| ARC-001 | high | done | I | on-point | Archive reader port exists and is consumed by use case | - |
| ARC-002 | high | done | I | on-point | Markdown fetch port exists and is consumed by use case | - |
| ARC-003 | high | done | I | on-point | Post store port exists and is consumed by use case | - |
| ARC-004 | medium | pending | I | on-point | Core does not depend directly on concrete adapters | - |
| PAR-001 | high | done | O | on-point | Parse archive item into URL and UTC timestamp | - |
| PAR-002 | high | pending | B | boundary | Parse post_date with timezone conversion around day boundaries | - |
| PAR-003 | high | done | L | limit case | Reject invalid archive payloads | - |
| PAG-001 | high | done | O | on-point | Archive reader fetches pages with `limit=20` | - |
| PAG-002 | high | pending | B | boundary | Archive reader handles 19/20/21 item page transitions | - |
| PAG-003 | high | done | L | limit case | Archive reader advances offset by observed page size | - |
| PAG-004 | medium | done | M | on-point | Archive reader deduplicates repeated canonical URLs | - |
| REP-001 | high | done | O | on-point | Upsert creates `timestamp-slug.md` for new post | - |
| REP-002 | high | done | B | boundary | Upsert renames legacy `slug.md` when hash matches | - |
| REP-003 | high | pending | B | boundary | Upsert updates content when hash differs | - |
| REP-004 | high | pending | L | limit case | Upsert consolidates duplicate files for same slug | - |
| REP-005 | medium | pending | L | limit case | Existing slug discovery supports legacy and timestamped names | - |
| USE-001 | high | done | O | on-point | Use case sync downloads new post and updates summary counts | - |
| USE-002 | high | done | B | boundary | Use case skips unchanged post when hash matches | - |
| USE-003 | high | pending | B | boundary | Use case continues after recoverable domain failure | - |
| USE-004 | medium | pending | L | limit case | Use case handles empty archive result | - |
| RES-001 | high | done | O | on-point | Retry policy sets max retries to 3 with 429 support | - |
| RES-002 | high | pending | B | boundary | Retry policy retries transient failures and succeeds within max retries | - |
| RES-003 | high | pending | L | limit case | Retry policy fails after max retries on persistent 429 | - |
| RES-004 | high | pending | L | limit case | Retry policy respects `Retry-After` header | - |
| RES-005 | medium | done | E | on-point | Circuit breaker opens on failure threshold and fails fast | - |
| RES-006 | medium | done | I | on-point | Null circuit breaker implementation exists for core flow wiring | - |
| CLI-001 | high | pending | O | on-point | CLI uses archive URL path by default | - |
| CLI-002 | medium | pending | B | boundary | CLI fallback alias from `--feed-url` to archive path remains compatible | - |
| CLI-003 | medium | pending | E | on-point | CLI returns failure code on unexpected errors | - |
| SCR-001 | high | done | O | on-point | Script maps `SUBSTACK_ARCHIVE_API_URL` to `--archive-url` | - |
| SCR-002 | medium | pending | L | limit case | Script ignores missing optional environment variables | - |
| WF-001 | high | done | I | on-point | Sync workflow uses archive proxy URL and explicit permissions | - |
| WF-002 | high | done | I | on-point | Quality workflow runs `make quality-ci` and no mutation commands | - |
| CON-001 | medium | pending | M | on-point | Contract removes legacy path only after migration validation passes | - |
| MUT-001 | high | done | E | on-point | Placeholder for next surviving mutant after mutation-gate | - |

## Mutation survivors log

Add one entry per survivor immediately after each mutation run, then create matching `MUT-*` backlog items.

| Date | Mutant ID | File | Reason | Action | Result |
| --- | --- | --- | --- | --- | --- |
| 2026-03-04 | none | n/a | mutation gate reported no surviving mutants | no follow-up required | closed |

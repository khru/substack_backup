# ADR-0005: Cursor pagination and markdown fallback

- Status: accepted
- Date: 2026-11-09
- Deciders: repository maintainers

## Context

The archive proxy now forwards to a Substack API that rejects offset pagination. The existing markdown converter can also become unavailable while source pages remain accessible.

## Decision

- Use the archive API's `nextCursor` pagination protocol with a page size of 20.
- Keep the worker markdown converter as the primary adapter.
- Fall back to Jina Reader's markdown response when the primary converter fails.
- Do not gate scheduled work on the wall-clock hour; delayed GitHub schedules must still execute.

## Consequences

- Every archive cursor page is traversed, including newly published articles.
- A temporary outage of the primary converter does not stop synchronization.
- The sync depends on a second external markdown service as a fallback.

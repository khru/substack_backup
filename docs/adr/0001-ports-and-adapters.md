# ADR-0001: Use Ports and Adapters in sync core

- Status: accepted
- Date: 2026-03-04
- Deciders: repository maintainers

## Context

Sync behavior depends on changing integration boundaries (Substack archive source, markdown endpoint, filesystem, CI workflow). Coupling domain use cases to concrete adapters increases migration cost.

## Decision

Adopt Ports and Adapters architecture:

- Core use cases depend on protocol-style ports.
- HTTP, filesystem, CLI, and workflow wiring live in adapters.
- Domain models remain immutable where possible.
- Null Object implementations are preferred over `None` flow-control in core paths.

## Consequences

### Positive

- Adapter changes do not force core rewrites.
- Testing is faster with boundary fakes.
- Parallel change migrations are safer.

### Negative

- Additional abstractions and wiring are required.

### Follow-up actions

- Keep protocol interfaces focused and stable.
- Add or update adapters incrementally using expand-migrate-contract.

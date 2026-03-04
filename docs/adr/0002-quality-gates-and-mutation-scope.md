# ADR-0002: Local mutation gate, CI quality-ci gate

- Status: accepted
- Date: 2026-03-04
- Deciders: repository maintainers

## Context

Mutation testing is mandatory for robust refactors, but it is expensive and unstable for hosted CI timing constraints.

## Decision

- Local completed refactor cycles must run `make mutation-gate`.
- CI workflows must run `make quality-ci` and must never execute mutation commands.
- A cycle cannot advance with non-equivalent surviving mutants.

## Consequences

### Positive

- CI remains fast and deterministic.
- Local development enforces strong behavioral test quality.

### Negative

- Developers must run additional local commands before closing cycles.

### Follow-up actions

- Keep tooling tests that verify workflow and Makefile policy alignment.

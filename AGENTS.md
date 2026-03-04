# AGENTS.md

## Scope and priority
- This file defines mandatory rules for autonomous coding agents in this repository.
- Follow this file unless a more local rule file overrides it.
- Override order: `.cursorrules` -> `.cursor/rules/**` -> `.github/copilot-instructions.md` -> `AGENTS.md`.

## Repository context
- Stack: Python 3.11+.
- Dependency and command management: `uv`.
- Test runner: `pytest` (existing tests can remain `unittest` style).
- Main paths:
  - `scripts/sync_substack.py`
  - `scripts/backup_post_images.py`
  - `src/substack_sync/`
  - `tests/`
  - `docs/adr/`
  - `docs/tdd/live-test-list.md`
  - `.github/workflows/substack-sync.yml`
  - `.github/workflows/substack-image-backup.yml`
  - `.github/workflows/quality.yml`

## Rule files status
- At snapshot time this repo has no:
  - `.cursorrules`
  - `.cursor/rules/`
  - `.github/copilot-instructions.md`
- Agents must re-check these paths before edits.

## Mandatory development contract

### TDD cycle (non-negotiable)
1. Red: write one focused failing test.
2. Validate Red: confirm it fails for the expected reason.
3. Green: implement the smallest change to pass.
4. Refactor: improve design and readability.
5. Run full quality gate.
6. Commit cycle result with Conventional Commit.
- Exactly one focused failing test per Red step.
- Never write production code without a failing test that requires it.
- Work test-by-test. Avoid bundling unrelated behavior.
- After each production code change, run the smallest relevant test set.
- Green must be the smallest possible implementation that satisfies the failing test.
- Refactor must include tidyings in test code, production code, and configuration when needed.
- Skipping tests to make the suite pass is forbidden.
- Deleting tests is forbidden unless the corresponding behavior is intentionally removed and replacement coverage is added.

### Live test list protocol (mandatory)
- Before starting implementation, create or refresh `docs/tdd/live-test-list.md`.
- The live test list is the single source of truth for execution order.
- Every item must include:
  - ID
  - Priority
  - Status (`pending`, `in_progress`, `done`, `blocked`)
  - ZOMBIES category (`Z`, `O`, `M`, `B`, `I`, `E`, `S`)
  - Case type (`on-point`, `boundary`, `limit case`)
  - Related commit hash after completion.
- End of each refactor phase must reprioritize the live test list before the next cycle starts.
- Any new risk, smell, or mutant survivor must add new live-list items immediately.

### Triangulation and Rule of Three (mandatory)
- Use triangulation to earn abstractions from multiple concrete examples.
- Do not generalize after a single example.
- Prefer Rule of Three:
  1. First time: implement directly.
  2. Second time: notice duplication but keep behavior concrete.
  3. Third time: refactor to a stable abstraction.
- Avoid speculative abstractions, generic base classes, or framework-like indirection before tests force them.
- During refactor, prioritize readability and low cognitive load over cleverness.

### Refactor phase must include mutation testing
- During Refactor, mutation testing is mandatory.
- Mutation testing is local-only and must not be executed in GitHub Actions pipelines.
- Run `make mutation-gate` and do not close the cycle if mutants survive.
- Goal: kill all possible mutants.
- If a mutant is equivalent, document why explicitly before accepting it.
- If mutants survive, add dedicated tests to the live test list and resolve them before moving to the next planned test.

### Planning rigor protocol (mandatory)
- Before implementation, write an explicit plan.
- The plan must include objective, constraints, risks, test strategy (Red/Green/Refactor), and validation commands.
- Map each planned behavior change to at least one focused failing test.
- Execute the plan step by step and report any deviation with rationale.
- A task is incomplete until planned validations pass or blockers are explicitly documented.

### ADR-first protocol (mandatory)
- Before creating the plan for any task, read all ADR files in `docs/adr/`.
- Plan decisions must align with accepted ADRs.
- If a refactor introduces or changes architectural decisions, write/update an ADR in the same cycle.
- README must link to ADRs and explain how they guide implementation.

### Parallel change protocol (mandatory for most refactors)
- For most refactors, when technically feasible, use Parallel Change with:
  1. Expand: add the new path while preserving compatibility with the existing path.
  2. Migrate: move callers, data, and workflows incrementally to the new path.
  3. Contract: remove the legacy path only after migration validations pass.
- Do not combine Expand and Contract in the same cycle unless the change is trivial and fully covered by focused tests.
- Each phase must include focused tests and explicit rollback notes.
- Parallel change is mandatory for API changes, shared contracts, persistent data formats, integration boundaries, and architectural seams.

### Commit policy
- One commit per completed TDD cycle.
- Immediately create a commit at the end of every completed TDD cycle.
- A cycle is not complete until the commit exists in git history.
- Include all changes produced in the current TDD cycle in the commit.
- Use Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `chore:`).
- Do not amend commits unless explicitly requested.

### Trunk-based development git sync protocol (mandatory)
- Use trunk-based development on `main`.
- Always run `git pull` before starting work.
- Before every push, run `git pull --rebase`.
- Resolve rebase conflicts locally, then rerun required validations before pushing.

## Tooling baseline
- Use `uv` for all dependency setup and command execution.
- Do not use `requirements*.txt` in this repository.
- Do not use `pip install -r ...` as project workflow.
- Install dev dependencies with:
  - `make install-dev`

## Build, lint, static analysis, and test commands
- Install dev tooling: `make install-dev`
- Build: `make build`
- Format: `make format`
- Format check: `make format-check`
- Lint: `make lint`
- Typecheck: `make typecheck`
- Tests: `make test`
- Mutation run: `make mutation`
- Mutation survivors report: `make mutation-report`
- Mutation gate: `make mutation-gate`
- Full local quality gate: `make quality`
- CI quality gate (no mutation): `make quality-ci`
- Local image backup run: `make backup-images`

## Required local quality gate order
Run commands in this exact order:
1. `make format-check`
2. `make lint`
3. `make typecheck`
4. `make test`
5. `make mutation-gate`
- If any command fails, the cycle is incomplete.

## Required CI quality gate order
Run commands in this exact order:
1. `make format-check`
2. `make lint`
3. `make typecheck`
4. `make test`
- CI must not execute mutation commands.

## Single-test quick reference (pytest)
- File:
  - `uv run pytest tests/test_use_case.py -q`
- Class:
  - `uv run pytest tests/test_use_case.py::SyncSubstackPostsUseCaseTests -q`
- Single test:
  - `uv run pytest tests/test_use_case.py::SyncSubstackPostsUseCaseTests::test_downloads_only_new_posts_returns_expected_summary -q`

## GitHub Actions policy

### Workflow permissions must be explicit
- Sync workflow (`.github/workflows/substack-sync.yml`) must declare:
  - `permissions: contents: write`
- Image backup workflow (`.github/workflows/substack-image-backup.yml`) must declare:
  - `permissions: contents: write`
- Quality workflow (`.github/workflows/quality.yml`) must declare:
  - `permissions: contents: read`
- Keep minimum required scope for each workflow.

### Mutation execution scope (mandatory)
- GitHub pipelines must never execute `mutmut`, `make mutation`, or `make mutation-gate`.
- Quality workflow must run `make quality-ci`.
- Mutation testing remains mandatory in local refactor phases.
- Do not close refactor work while any non-equivalent mutant survives.

### Local workflow validation with act
- `act` validation is mandatory when workflow files change.
- Required checks:
  1. `make act-list`
  2. `make act-dispatch`
  3. `make act-schedule`
  4. `make act-image-dispatch` when image backup workflow changes
- Local workflow runs should use `skip_repo_steps=true` or `SKIP_REPO_STEPS=true` when commit/push is not needed.

## Sync pipeline invariants
- Execute at 09:00 Europe/Madrid (cron in UTC + guard).
- Primary source is archive API via worker proxy with pagination.
- Default archive page size is `limit=20` and pagination must advance with observed page size.
- Keep markdown endpoint: `https://substack-to-markdown.evalverde.workers.dev/?url=<encoded-url>`.
- Output path format is `posts/<timestamp>-<slug>.md`.
- Timestamp format is UTC `YYYYMMDDHHMMSS`.
- Compare content hashes (MD5) to decide update versus unchanged.
- Legacy `posts/<slug>.md` files must migrate without duplicates.
- If any required article cannot be downloaded, fail workflow.
- If markdown is empty, fail workflow.
- Never commit empty markdown files.
- Commit only when staged changes exist.

## Image backup invariants
- Image backup runs as an independent process from article synchronization.
- Source markdown must be read from `posts/*.md` only.
- Image output path format is `img/<markdown_stem>/`.
- Image backup must not rewrite markdown links.
- If no remote images are found, the process exits successfully without creating unnecessary files.
- The process must fail if any required image cannot be downloaded.
- Image commits must run only when staged changes exist in `img/`.

## Architecture and design rules
- Separation of concerns means separating by reasons to change.
- Keep volatile concerns isolated so business rules remain stable and testable.
- Apply separation of concerns by actions, calculations, and data.
  - Actions: HTTP, filesystem writes, git operations, logging.
  - Calculations: parsing, slug resolution, planning, summarization.
  - Data: immutable value objects and result objects.
- Keep calculations deterministic and free of side effects.
- Keep actions at the boundaries (imperative shell) and minimal.
- Make time and ordering explicit when actions depend on timing.
- Favor idempotent actions and explicit deduplication for repeated runs.
- Keep data structures intention-revealing (list for order, set for uniqueness, map for lookup).
- Enforce SOLID principles.
- Respect Law of Demeter.
- Apply Object Calisthenics where practical for readability and low coupling.
- Use encapsulation and dependency inversion.
- Use control inversion and dependency injection at boundaries.
- Use focused interfaces/ports (interface segregation).
- Use Ports and Adapters architecture for boundary integrations so adapters can evolve independently from core logic.
- Null Object pattern is mandatory in core flows.
- Prefer explicit result objects over `None` flow-control in core logic.
- Immutability is mandatory by default.
- Prefer immutable structures (`frozen=True`, tuples/frozensets) in domain/use-case flows.

## Typing policy (mandatory)
- All Python code must be fully typed.
- New or modified production and test code must include explicit type hints.
- `mypy` strict mode must pass for `src`, `scripts`, and `tests`.
- Avoid untyped escapes (`Any`) unless explicitly justified.

## Code and test smell policy

### Code smell catalog (mandatory)
- Follow the canonical refactoring catalog (2nd edition + relevant legacy smells).
- Required smells to detect and resolve include:
  - mysterious name
  - duplicated code
  - long function
  - long parameter list
  - global data
  - mutable data
  - divergent change
  - shotgun surgery
  - feature envy
  - data clumps
  - primitive obsession
  - repeated switches
  - loops with hidden intent
  - lazy element
  - speculative generality
  - temporary field
  - message chains
  - middle man
  - insider trading
  - large class
  - alternative classes with different interfaces
  - data class
  - refused bequest
  - comments masking unclear code
  - parallel inheritance hierarchies
  - incomplete library class

### Test design quality principles (mandatory)
- FIRST principles are mandatory:
  - fast
  - independent
  - repeatable
  - self-validating
  - timely
- Test desiderata are mandatory:
  - behavior-focused
  - precise failure diagnostics
  - maintainable structure
  - low cognitive load
  - resilience against harmless refactors
- Every behavior change must include on-point, boundary, and limit case coverage.
- Prefer one clear intention per test.
- Use constants and variables in tests as locally as possible unless parametrization or shared fixture value adds clarity.

### Test smells catalog (mandatory)
- assertion roulette: multiple unrelated assertions hide failure intent; split tests or add clearer checks.
- conditional test logic: avoid branching in tests; separate scenarios into independent tests.
- constructor initialization: initialize shared setup through framework setup hooks.
- default test: remove generated placeholder tests that carry no domain intent.
- duplicate assert: avoid repeated identical assertions in a single test.
- eager test: avoid validating many behaviors in one test method.
- empty test: remove or implement immediately; no empty shells.
- exception handling in tests with manual try/catch: use framework assertion helpers for exceptions.
- general fixture: avoid broad setup used by only a subset of tests.
- ignored test: do not keep disabled tests indefinitely.
- lazy test: avoid low-value tests repeating same behavior without meaningful variation.
- magic number test: replace unexplained literals with intention-revealing names.
- mystery guest: avoid hidden external dependencies in test setup.
- redundant print: remove debug printing from automated tests.
- redundant assertion: remove assertions that cannot fail meaningfully.
- resource optimism: create or fake required resources explicitly; never assume presence.
- sensitive equality: assert domain state or semantic equality, not unstable formatting.
- sleepy test: avoid fixed sleeps; use condition-based waiting helpers.
- unknown test: each test must verify an observable outcome explicitly.
- Prevent these smells proactively and refactor immediately when detected.

### Parallel change recipes for smells
- Use parallel change recipes when fixing public or shared contracts:
  - rename/signature migration recipe
  - parameter object/value object extraction recipe
  - repeated switch to polymorphism recipe
  - inheritance to delegation recipe
  - global/mutable state encapsulation recipe
- For purely local refactors, keep changes small and direct.

## Code style guidelines

### Imports and module boundaries
- Use explicit imports only; no wildcard imports.
- Group imports: standard library, third-party, local modules.
- Keep import groups sorted unless tool says otherwise.
- Remove unused imports immediately.

### Formatting and readability
- Formatter output is source of truth.
- Keep functions focused and small.
- Replace magic literals with named constants.
- Add comments only when intent is not obvious.
- Prefer guard clauses over deep nesting.

### Naming conventions
- Classes/types: `PascalCase`.
- Functions/variables/modules: `snake_case`.
- Constants/env keys: `UPPER_SNAKE_CASE`.
- Do not use abbreviations in names.
- Names must reveal intent.
- Tests must describe behavior, not implementation details.

### Error handling
- Fail fast with actionable boundary errors.
- Never swallow exceptions silently.
- Preserve context when re-raising.
- Separate expected domain failures from unexpected failures.

### Testing conventions
- Add or update tests for each behavior change.
- Prefer deterministic tests; avoid flaky time/network dependencies.
- Mock only boundaries (HTTP, filesystem, clock).
- Keep assertions focused so each test fails for one primary reason when practical.
- Treat tests as first-class clients of the design.
- Refactor tests in the Refactor phase to keep naming and intent clear.
- Do not use `skip`/`xfail` as a workaround for failing behavior.
- If a test must be removed, document the removed behavior and add equivalent behavioral coverage in the same cycle.

### Dead code policy
- Remove code paths, methods, and branches that are no longer used.
- Keep project warning-free under lint and static analysis for unused elements.
- Delete superseded abstractions in the same refactor.

## Agent workflow expectations
- Keep diffs focused and minimal.
- Avoid unrelated refactors in the same change.
- If tooling is missing, report exact install steps.
- Report commands executed and any blocked validations.

## Exit criteria before finishing work
- Build passes for touched code.
- Full quality gate passes.
- Workflow changes validated with `act` (or clearly reported as blocked).
- Acceptance criteria and constraints are satisfied.

## Maintenance
- Update this file when tooling/scripts/workflows change.
- Keep command references exact and runnable.
- Keep this document clear, strict, and practical.
- Keep README and AGENTS evolving with every relevant learning.

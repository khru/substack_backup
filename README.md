[![Sync Substack Posts](https://github.com/khru/substack_backup/actions/workflows/substack-sync.yml/badge.svg)](https://github.com/khru/substack_backup/actions/workflows/substack-sync.yml)
[![Quality Gate](https://github.com/khru/substack_backup/actions/workflows/quality.yml/badge.svg)](https://github.com/khru/substack_backup/actions/workflows/quality.yml)

# Substack Backup Sync

## Why this project exists

This project exists to keep a versioned markdown backup of Substack articles in git, including future edits to already published posts.

## Problem it solves

GitHub-hosted runners can be blocked when calling Substack endpoints directly. The sync workflow must still:

- fetch the complete article history,
- detect when an article changed,
- persist updates with deterministic filenames,
- and keep a reliable local quality process with mutation testing.

The repository solves this by using a Cloudflare Worker archive proxy, MD5 content comparison, and timestamped filenames.

## What the sync does

- Reads article metadata from archive API proxy pages (`limit=20`, offset pagination).
- Calls the markdown endpoint:
  - `https://substack-to-markdown.evalverde.workers.dev/?url=<URL_ENCODED>`
- Stores files in `posts/` as:
  - `posts/<YYYYMMDDHHMMSS>-<slug>.md`
- Compares markdown MD5 hashes to decide unchanged vs update.
- Migrates legacy `posts/<slug>.md` files without creating duplicates.
- Fails when required markdown cannot be downloaded or is empty.

## Image backup

The repository runs a separate image backup process for markdown posts.

- Scans `posts/*.md` and extracts remote image URLs.
- Downloads images to `img/<markdown_stem>/`.
- Keeps markdown content intact without rewriting markdown links.
- Fails the process if any required image cannot be downloaded.
- Commits only when new or updated files are staged in `img/`.

## Stack

- Language: Python 3.11+
- Package and command tooling: `uv`
- Test runner: `pytest` (tests may remain `unittest` style)
- Lint and format: `ruff`
- Static typing: `mypy` strict mode
- Mutation testing: `mutmut`

## Runtime resilience libraries

The sync pipeline relies on two runtime libraries for resilient HTTP execution:

- `urllib3`: retry/backoff support, including `429` and `Retry-After` handling.
- `pybreaker`: circuit breaker support for unstable integrations.

These libraries are documented and versioned to keep local and CI behavior aligned.

## ADRs

- ADR directory: `docs/adr`
- ADR index: `docs/adr/README.md`
- Current key decisions:
  - `docs/adr/0001-ports-and-adapters.md`
  - `docs/adr/0002-quality-gates-and-mutation-scope.md`
  - `docs/adr/0003-archive-api-and-timestamped-post-files.md`
  - `docs/adr/0004-independent-image-backup-and-local-asset-layout.md`

## Tooling and setup (`uv`)

1. Install `uv`.
2. Install development dependencies:

```bash
make install-dev
```

This command runs `uv sync --extra dev --no-install-project`.

## How to use

Run sync locally:

```bash
make sync
```

Run image backup locally:

```bash
make backup-images
```

Optional environment variables:

- `SUBSTACK_ARCHIVE_API_URL`
- `SUBSTACK_FEED_URL` (legacy alias)
- `SUBSTACK_MARKDOWN_ENDPOINT`
- `SUBSTACK_OUTPUT_DIR`
- `SUBSTACK_TIMEOUT_SECONDS`

Optional environment variables for image backup:

- `SUBSTACK_POSTS_DIR`
- `SUBSTACK_IMAGES_DIR`
- `SUBSTACK_TIMEOUT_SECONDS`

## Test and quality

Run tests:

```bash
make test
```

Run full local quality gate:

```bash
make quality
```

Local quality gate order:

1. `make format-check`
2. `make lint`
3. `make typecheck`
4. `make test`
5. `make mutation-gate`

Run CI quality gate locally (without mutation):

```bash
make quality-ci
```

## Mutation testing

Mutation testing is required during refactor phases and must run locally.

```bash
make mutation
make mutation-report
make mutation-gate
```

If `mutation-gate` fails, surviving mutants must be killed with additional/refined tests or documented as equivalent only when unavoidable.

## Typing policy

All Python code must be typed.

- Static typing is enforced with strict `mypy`.
- New or modified production code and test code must include explicit type hints.

## GitHub Actions

### Sync workflow

Workflow: `.github/workflows/substack-sync.yml`

- Runs on `workflow_dispatch` and schedule (`0 7,8 * * *` UTC).
- Uses timezone guard so schedule executes at 09:00 `Europe/Madrid`.
- Uses archive proxy via `SUBSTACK_ARCHIVE_API_URL`.
- Commits only when staged markdown changes exist.
- Validates staged markdown files are non-empty.
- Supports `skip_repo_steps=true` for local workflow validation.
- Declares explicit write permission:
  - `permissions: contents: write`

### Quality workflow

Workflow: `.github/workflows/quality.yml`

- Runs on `workflow_dispatch`, `push`, and `pull_request`.
- Installs dependencies with `uv`.
- Runs `make quality-ci` (format-check, lint, typecheck, test; no mutation in CI).
- Declares minimal read permission:
  - `permissions: contents: read`

### Image backup workflow

Workflow: `.github/workflows/substack-image-backup.yml`

- Runs on `workflow_dispatch` and `push` when `posts/*.md` changes.
- Installs dependencies with `uv`.
- Runs `uv run python scripts/backup_post_images.py`.
- Fails if any required image cannot be downloaded.
- Stores assets in `img/<markdown_stem>/` without rewriting markdown links.
- Declares explicit write permission:
  - `permissions: contents: write`

## Local workflow testing with `act`

Install `act`: <https://github.com/nektos/act>

```bash
make act-list
make act-dispatch
make act-schedule
make act-image-dispatch
```

`make act-dispatch` and `make act-schedule` skip repository commit/push steps via `skip_repo_steps` and `SKIP_REPO_STEPS` so workflow logic can be validated safely in local containers.

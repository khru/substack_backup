# Substack Backup Pipeline

This repository downloads posts from a Substack RSS feed and stores each article as markdown in `posts/`.

## What the sync does

- Reads feed URLs from `https://emmanuelvalverderamos.substack.com/feed.xml`.
- Calls the markdown endpoint as:
  - `https://substack-to-markdown.evalverde.workers.dev/?url=<URL_ENCODED>`
- Uses slug-based filenames under `posts/`: `posts/<slug>.md`.
- Skips already downloaded slugs.
- Fails when a new article cannot be downloaded.
- Fails when downloaded markdown is empty.

## Tooling and setup (uv)

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency and command management.

1. Install `uv`.
2. Install development dependencies:

```bash
make install-dev
```

This command runs `uv sync --extra dev --no-install-project`.

## Run locally

Run sync locally:

```bash
make sync
```

Optional environment variables:

- `SUBSTACK_FEED_URL`
- `SUBSTACK_MARKDOWN_ENDPOINT`
- `SUBSTACK_OUTPUT_DIR`
- `SUBSTACK_TIMEOUT_SECONDS`

## Test and quality

Run tests with `pytest` (current tests remain in `unittest` style, executed by pytest):

```bash
make test
```

Run full quality gate:

```bash
make quality
```

Quality gate runs:

1. `make format-check`
2. `make lint`
3. `make typecheck`
4. `make test`
5. `make mutation-gate`

## Mutation testing

Mutation testing is done with `mutmut` and is required during refactor.

Commands:

```bash
make mutation
make mutation-report
make mutation-gate
```

If `mutation-gate` fails, surviving mutants must be killed with additional/refined tests (or documented as equivalent mutants when truly unavoidable).
Skipping or deleting tests to pass mutation testing is not allowed.

## Typing policy

All Python code must be fully typed, including production code and tests.

- Static typing is enforced with strict `mypy`.
- New or modified Python code is expected to include explicit type hints.

## GitHub Actions

### Sync workflow

Workflow: `.github/workflows/substack-sync.yml`

- Runs on `workflow_dispatch` and schedule (`0 7,8 * * *` UTC).
- Uses timezone guard so schedule executes at 09:00 `Europe/Madrid`.
- Commits only when staged markdown changes exist.
- Validates staged markdown files are not empty.
- Supports `skip_repo_steps=true` for local testing.
- Declares explicit write permission:
  - `permissions: contents: write`

### Quality workflow

Workflow: `.github/workflows/quality.yml`

- Runs on `workflow_dispatch`, `push`, and `pull_request`.
- Installs dependencies with `uv`.
- Runs `make quality-ci` (format-check, lint, typecheck, test; no mutation in CI).
- Declares minimal read permission:
  - `permissions: contents: read`

## Use this in your own GitHub repository

1. Push all files, including workflows, `scripts/`, and `src/`.
2. Update `SUBSTACK_FEED_URL` in `.github/workflows/substack-sync.yml`.
3. Keep or replace `SUBSTACK_MARKDOWN_ENDPOINT` if you host your own converter.
4. In repo settings, enable workflow write permission for sync commits:
   - `Settings -> Actions -> General -> Workflow permissions -> Read and write permissions`.
5. If your default branch is protected, allow this workflow to push or use a PR flow.
6. Trigger `workflow_dispatch` once and verify outputs in `posts/`.

## Local workflow testing with act

Install `act`: https://github.com/nektos/act

```bash
make act-list
make act-dispatch
make act-schedule
```

`make act-dispatch` and `make act-schedule` skip repository commit/push steps via `skip_repo_steps`/`SKIP_REPO_STEPS` so workflow logic can be validated safely in local containers.

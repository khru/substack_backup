ACT ?= $(HOME)/.local/bin/act
SRC_DIRS := src tests scripts
WORKFLOW_FILE := .github/workflows/substack-sync.yml

.PHONY: build lint test format format-check typecheck quality sync install-dev mutation mutation-report mutation-gate act-list act-dispatch act-schedule

define run_act
	@if ! command -v docker >/dev/null 2>&1; then \
		echo "Docker is not installed; skipping act command: $(1)"; \
		exit 0; \
	fi
	@if ! docker info >/dev/null 2>&1; then \
		echo "Docker daemon is not available; skipping act command: $(1)"; \
		exit 0; \
	fi
	$(ACT) $(1)
endef

install-dev:
	uv sync --extra dev --no-install-project

build:
	uv run python -m compileall src scripts

lint:
	uv run ruff check $(SRC_DIRS)

format:
	uv run ruff format $(SRC_DIRS)

format-check:
	uv run ruff format --check $(SRC_DIRS)

typecheck:
	PYTHONPATH=src uv run mypy src scripts/sync_substack.py tests

test:
	PYTHONPATH=src uv run pytest

mutation:
	PYTHONPATH=src uv run mutmut run

mutation-report:
	PYTHONPATH=src uv run mutmut results

mutation-gate: mutation
	@results="$$(PYTHONPATH=src uv run mutmut results)"; \
	if [ -n "$$results" ]; then \
		echo "Surviving mutants detected."; \
		echo "$$results"; \
		exit 1; \
	fi

quality: format-check lint typecheck test mutation-gate

sync:
	PYTHONPATH=src uv run python scripts/sync_substack.py

act-list:
	$(call run_act,-l)

act-dispatch:
	$(call run_act,workflow_dispatch -W $(WORKFLOW_FILE) -j sync-substack --input skip_repo_steps=true --rm)

act-schedule:
	$(call run_act,schedule -W $(WORKFLOW_FILE) -j sync-substack --env SKIP_REPO_STEPS=true --rm)

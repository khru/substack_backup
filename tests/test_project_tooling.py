from __future__ import annotations

import tomllib
import unittest
from pathlib import Path


def _discover_project_root() -> Path:
    required_files = ("pyproject.toml", "AGENTS.md", "README.md", "Makefile")

    search_roots = [Path.cwd(), *Path.cwd().parents, *Path(__file__).resolve().parents]
    for candidate in search_roots:
        if all((candidate / required_file).exists() for required_file in required_files):
            return candidate

    raise FileNotFoundError("Unable to locate project root with required metadata files")


_PROJECT_ROOT = _discover_project_root()
_PYPROJECT_PATH = _PROJECT_ROOT / "pyproject.toml"
_EDITORCONFIG_PATH = _PROJECT_ROOT / ".editorconfig"
_MAKEFILE_PATH = _PROJECT_ROOT / "Makefile"
_SETUP_CFG_PATH = _PROJECT_ROOT / "setup.cfg"
_README_PATH = _PROJECT_ROOT / "README.md"
_AGENTS_PATH = _PROJECT_ROOT / "AGENTS.md"
_SCRIPT_PATH = _PROJECT_ROOT / "scripts/sync_substack.py"
_ADR_DIRECTORY_PATH = _PROJECT_ROOT / "docs/adr"
_ADR_README_PATH = _ADR_DIRECTORY_PATH / "README.md"
_ADR_TEMPLATE_PATH = _ADR_DIRECTORY_PATH / "0000-template.md"
_LIVE_TEST_LIST_PATH = _PROJECT_ROOT / "docs/tdd/live-test-list.md"
_SYNC_WORKFLOW_PATH = _PROJECT_ROOT / ".github/workflows/substack-sync.yml"
_QUALITY_WORKFLOW_PATH = _PROJECT_ROOT / ".github/workflows/quality.yml"
_REQUIREMENTS_DEV_PATH = _PROJECT_ROOT / "requirements-dev.txt"


class ProjectToolingTests(unittest.TestCase):
    def test_editorconfig_exists_with_basic_defaults(self) -> None:
        content = _EDITORCONFIG_PATH.read_text(encoding="utf-8")

        self.assertIn("root = true", content)
        self.assertIn("charset = utf-8", content)
        self.assertIn("indent_style = space", content)
        self.assertIn("indent_size = 4", content)
        self.assertIn("end_of_line = lf", content)
        self.assertIn("insert_final_newline = true", content)

    def test_requirements_dev_file_is_not_used(self) -> None:
        self.assertFalse(_REQUIREMENTS_DEV_PATH.exists())

    def test_pyproject_declares_core_dev_tooling_dependencies(self) -> None:
        pyproject_data = tomllib.loads(_PYPROJECT_PATH.read_text(encoding="utf-8"))
        optional_dependencies = pyproject_data["project"]["optional-dependencies"]
        dev_dependencies = optional_dependencies["dev"]

        self.assertIn("ruff", dev_dependencies)
        self.assertIn("mypy", dev_dependencies)
        self.assertIn("vulture", dev_dependencies)

    def test_pyproject_declares_pytest_and_mutation_testing_dependencies(self) -> None:
        pyproject_data = tomllib.loads(_PYPROJECT_PATH.read_text(encoding="utf-8"))
        optional_dependencies = pyproject_data["project"]["optional-dependencies"]
        dev_dependencies = optional_dependencies["dev"]

        self.assertIn("pytest", dev_dependencies)
        self.assertIn("mutmut", dev_dependencies)

    def test_pyproject_declares_runtime_resilience_dependencies(self) -> None:
        pyproject_data = tomllib.loads(_PYPROJECT_PATH.read_text(encoding="utf-8"))
        dependencies = pyproject_data["project"]["dependencies"]

        self.assertIn("urllib3", dependencies)
        self.assertIn("pybreaker", dependencies)

    def test_makefile_install_dev_uses_uv_sync(self) -> None:
        makefile_content = _MAKEFILE_PATH.read_text(encoding="utf-8")

        self.assertIn("uv sync --extra dev", makefile_content)

    def test_makefile_uses_uv_run_for_quality_commands(self) -> None:
        makefile_content = _MAKEFILE_PATH.read_text(encoding="utf-8")

        self.assertIn("uv run", makefile_content)

    def test_makefile_exposes_mutation_targets(self) -> None:
        makefile_content = _MAKEFILE_PATH.read_text(encoding="utf-8")

        self.assertIn("mutation:", makefile_content)
        self.assertIn("mutation-gate:", makefile_content)

    def test_makefile_separates_local_and_ci_quality_targets(self) -> None:
        makefile_content = _MAKEFILE_PATH.read_text(encoding="utf-8")

        self.assertIn("quality-ci: format-check lint typecheck test", makefile_content)
        self.assertIn("quality: quality-ci mutation-gate", makefile_content)

    def test_mutmut_setup_copies_source_package_for_local_runs(self) -> None:
        setup_cfg_content = _SETUP_CFG_PATH.read_text(encoding="utf-8")

        self.assertIn("also_copy=", setup_cfg_content)
        self.assertIn("src/substack_sync", setup_cfg_content)

    def test_quality_workflow_exists(self) -> None:
        self.assertTrue(_QUALITY_WORKFLOW_PATH.exists())

    def test_sync_workflow_declares_contents_write_permission(self) -> None:
        workflow_content = _SYNC_WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("permissions:", workflow_content)
        self.assertIn("contents: write", workflow_content)

    def test_sync_workflow_uses_cloudflare_archive_proxy_url(self) -> None:
        workflow_content = _SYNC_WORKFLOW_PATH.read_text(encoding="utf-8")
        expected_archive_proxy_url = (
            "https://emmanuelvalverderamos-substack-api.evalverde.workers.dev/"
        )

        self.assertIn(
            f"SUBSTACK_ARCHIVE_API_URL: {expected_archive_proxy_url}",
            workflow_content,
        )
        self.assertNotIn(
            "SUBSTACK_FEED_URL: https://emmanuelvalverderamos.substack.com/feed.xml",
            workflow_content,
        )

    def test_sync_workflow_installs_runtime_dependencies_with_uv(self) -> None:
        workflow_content = _SYNC_WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("python -m pip install uv", workflow_content)
        self.assertIn("uv sync --no-install-project", workflow_content)
        self.assertIn("uv run python scripts/sync_substack.py", workflow_content)

    def test_sync_script_supports_archive_api_environment_variable(self) -> None:
        script_content = _SCRIPT_PATH.read_text(encoding="utf-8")

        self.assertIn("SUBSTACK_ARCHIVE_API_URL", script_content)
        self.assertIn("--archive-url", script_content)

    def test_quality_workflow_declares_contents_read_permission(self) -> None:
        workflow_content = _QUALITY_WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("permissions:", workflow_content)
        self.assertIn("contents: read", workflow_content)

    def test_quality_workflow_runs_ci_quality_target(self) -> None:
        workflow_content = _QUALITY_WORKFLOW_PATH.read_text(encoding="utf-8")
        run_lines = [
            line.strip()
            for line in workflow_content.splitlines()
            if line.strip().startswith("run:")
        ]

        self.assertIn("run: make quality-ci", run_lines)
        self.assertNotIn("run: make quality", run_lines)

    def test_workflows_do_not_execute_mutation_commands(self) -> None:
        workflow_paths = (_SYNC_WORKFLOW_PATH, _QUALITY_WORKFLOW_PATH)

        for workflow_path in workflow_paths:
            workflow_content = workflow_path.read_text(encoding="utf-8").lower()
            self.assertNotIn("mutmut", workflow_content)
            self.assertNotIn("make mutation", workflow_content)
            self.assertNotIn("mutation-gate", workflow_content)

    def test_readme_documents_uv_pytest_mutation_and_typing(self) -> None:
        readme_content = _README_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("uv", readme_content)
        self.assertIn("pytest", readme_content)
        self.assertIn("mutmut", readme_content)
        self.assertIn("typed", readme_content)

    def test_readme_documents_ci_quality_gate_without_mutation(self) -> None:
        readme_content = _README_PATH.read_text(encoding="utf-8")

        self.assertIn("make quality-ci", readme_content)
        self.assertNotIn("- Runs `make quality`.", readme_content)

    def test_readme_documents_resilience_libraries(self) -> None:
        readme_content = _README_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("urllib3", readme_content)
        self.assertIn("pybreaker", readme_content)

    def test_readme_displays_sync_and_quality_badges(self) -> None:
        readme_content = _README_PATH.read_text(encoding="utf-8")

        self.assertIn(
            "[![Sync Substack Posts](https://github.com/khru/substack_backup/actions/workflows/substack-sync.yml/badge.svg)](https://github.com/khru/substack_backup/actions/workflows/substack-sync.yml)",
            readme_content,
        )
        self.assertIn(
            "[![Quality Gate](https://github.com/khru/substack_backup/actions/workflows/quality.yml/badge.svg)](https://github.com/khru/substack_backup/actions/workflows/quality.yml)",
            readme_content,
        )

    def test_readme_documents_project_purpose_stack_usage_and_adr_links(self) -> None:
        readme_content = _README_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("why this project exists", readme_content)
        self.assertIn("problem it solves", readme_content)
        self.assertIn("stack", readme_content)
        self.assertIn("how to use", readme_content)
        self.assertIn("docs/adr", readme_content)

    def test_docs_include_adr_and_live_test_list_scaffolding(self) -> None:
        self.assertTrue(_ADR_DIRECTORY_PATH.exists())
        self.assertTrue(_ADR_README_PATH.exists())
        self.assertTrue(_ADR_TEMPLATE_PATH.exists())
        self.assertTrue(_LIVE_TEST_LIST_PATH.exists())

    def test_agents_documents_uv_pytest_mutation_and_typing(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("uv", agents_content)
        self.assertIn("pytest", agents_content)
        self.assertIn("mutation", agents_content)
        self.assertIn("typed", agents_content)

    def test_agents_enforces_commit_after_each_completed_tdd_cycle(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn(
            "immediately create a commit at the end of every completed tdd cycle",
            agents_content,
        )
        self.assertIn(
            "a cycle is not complete until the commit exists in git history",
            agents_content,
        )

    def test_agents_requires_cycle_commit_to_include_all_cycle_changes(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn(
            "include all changes produced in the current tdd cycle in the commit",
            agents_content,
        )

    def test_agents_requires_rigorous_plan_before_execution(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("planning rigor protocol (mandatory)", agents_content)
        self.assertIn("before implementation, write an explicit plan", agents_content)

    def test_agents_requires_parallel_change_for_most_refactors(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("parallel change protocol", agents_content)
        self.assertIn("expand", agents_content)
        self.assertIn("migrate", agents_content)
        self.assertIn("contract", agents_content)

    def test_agents_requires_pull_before_start_and_rebase_before_push(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("trunk-based development", agents_content)
        self.assertIn("always run `git pull` before starting work", agents_content)
        self.assertIn("before every push, run `git pull --rebase`", agents_content)

    def test_agents_separates_local_and_ci_mutation_execution(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn(
            "github pipelines must never execute `mutmut`, `make mutation`, "
            "or `make mutation-gate`",
            agents_content,
        )
        self.assertIn("mutation testing remains mandatory in local refactor phases", agents_content)
        self.assertIn("goal: kill all possible mutants", agents_content)

    def test_agents_forbids_abbreviated_names(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("do not use abbreviations", agents_content)
        self.assertIn("names must reveal intent", agents_content)

    def test_agents_requires_single_failing_test_per_red_step(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("exactly one focused failing test per red step", agents_content)

    def test_agents_requires_test_execution_after_each_change(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn(
            "after each production code change, run the smallest relevant test set", agents_content
        )

    def test_agents_makes_null_object_and_immutability_mandatory(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("null object pattern is mandatory in core flows", agents_content)
        self.assertIn("immutability is mandatory by default", agents_content)

    def test_agents_documents_test_quality_principles_and_test_smells_catalog(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        self.assertIn("first principles", agents_content)
        self.assertIn("test desiderata", agents_content)
        self.assertIn("live test list", agents_content)
        self.assertIn("on-point", agents_content)
        self.assertIn("boundary", agents_content)
        self.assertIn("limit case", agents_content)

        required_test_smells = (
            "assertion roulette",
            "conditional test logic",
            "constructor initialization",
            "default test",
            "duplicate assert",
            "eager test",
            "empty test",
            "exception handling",
            "general fixture",
            "ignored test",
            "lazy test",
            "magic number test",
            "mystery guest",
            "redundant print",
            "redundant assertion",
            "resource optimism",
            "sensitive equality",
            "sleepy test",
            "unknown test",
        )

        for test_smell in required_test_smells:
            self.assertIn(test_smell, agents_content)

    def test_agents_documents_required_architecture_and_code_smell_rules(self) -> None:
        agents_content = _AGENTS_PATH.read_text(encoding="utf-8").lower()

        required_architecture_rules = (
            "separation of concerns",
            "solid",
            "law of demeter",
            "object calisthenics",
            "actions",
            "calculations",
            "data",
            "control inversion",
            "dependency inversion",
            "interface segregation",
            "ports and adapters architecture",
            "encapsulation",
        )

        required_code_smells = (
            "data clumps",
            "primitive obsession",
            "mysterious name",
            "duplicated code",
            "long function",
            "long parameter list",
            "global data",
            "mutable data",
            "feature envy",
            "message chains",
            "middle man",
            "insider trading",
            "large class",
            "alternative classes with different interfaces",
            "data class",
            "refused bequest",
            "parallel inheritance hierarchies",
            "incomplete library class",
        )

        for architecture_rule in required_architecture_rules:
            self.assertIn(architecture_rule, agents_content)

        for code_smell in required_code_smells:
            self.assertIn(code_smell, agents_content)


if __name__ == "__main__":
    unittest.main()

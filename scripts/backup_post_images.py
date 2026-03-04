#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIRECTORY = PROJECT_ROOT / "src"


def _configure_python_path() -> None:
    source_directory_text = str(SOURCE_DIRECTORY)
    if source_directory_text not in sys.path:
        sys.path.insert(0, source_directory_text)


def _build_arguments_from_environment() -> list[str]:
    environment_mappings = {
        "SUBSTACK_POSTS_DIR": "--posts-directory",
        "SUBSTACK_IMAGES_DIR": "--images-directory",
        "SUBSTACK_TIMEOUT_SECONDS": "--timeout-seconds",
    }

    command_arguments: list[str] = []
    for environment_name, argument_name in environment_mappings.items():
        environment_value = os.getenv(environment_name)
        if environment_value is None:
            continue

        command_arguments.extend([argument_name, environment_value])

    return command_arguments


def main() -> int:
    _configure_python_path()
    from substack_sync.image_backup_cli import main as cli_main

    command_arguments = _build_arguments_from_environment()
    command_arguments.extend(sys.argv[1:])
    return cli_main(argv=command_arguments)


if __name__ == "__main__":
    raise SystemExit(main())

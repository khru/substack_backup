from __future__ import annotations

import os
import tempfile
from pathlib import Path

from substack_sync.image_backup_repository_port import ImageBackupRepository
from substack_sync.image_file_naming import build_image_file_name
from substack_sync.image_persistence_error import ImagePersistenceError


class FileSystemImageBackupRepository(ImageBackupRepository):
    def __init__(self, output_directory: Path) -> None:
        self._output_directory = output_directory

    def has_image(self, markdown_file_path: Path, image_url: str, image_index: int) -> bool:
        target_path = self._target_path(markdown_file_path, image_url, image_index)
        return target_path.exists() and target_path.is_file() and target_path.stat().st_size > 0

    def save_image(
        self,
        markdown_file_path: Path,
        image_url: str,
        image_index: int,
        image_content: bytes,
    ) -> Path:
        target_path = self._target_path(markdown_file_path, image_url, image_index)
        target_path.parent.mkdir(parents=True, exist_ok=True)

        file_descriptor, temporary_path_as_text = tempfile.mkstemp(
            prefix="image-",
            suffix=".tmp",
            dir=target_path.parent,
        )
        temporary_path = Path(temporary_path_as_text)

        try:
            with os.fdopen(file_descriptor, "wb") as stream:
                stream.write(image_content)

            if temporary_path.stat().st_size <= 0:
                raise ImagePersistenceError(f"Image file for {image_url} is empty.")

            temporary_path.replace(target_path)
        except OSError as error:
            raise ImagePersistenceError(f"Unable to persist image for {image_url}") from error
        finally:
            if temporary_path.exists():
                temporary_path.unlink()

        return target_path

    def _target_path(self, markdown_file_path: Path, image_url: str, image_index: int) -> Path:
        image_directory = self._output_directory / markdown_file_path.stem
        file_name = build_image_file_name(image_url=image_url, image_index=image_index)
        return image_directory / file_name

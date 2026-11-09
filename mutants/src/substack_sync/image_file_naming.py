from __future__ import annotations

import hashlib
import re
from urllib.parse import unquote

IMAGE_EXTENSION_PATTERN = re.compile(
    r"\.(png|jpe?g|gif|webp|svg|bmp|tiff?)(?:$|[?#])", re.IGNORECASE
)


def infer_image_extension(image_url: str) -> str:
    extension_match = _match_extension(image_url)
    if extension_match is not None:
        return extension_match

    once_decoded = unquote(image_url)
    extension_match = _match_extension(once_decoded)
    if extension_match is not None:
        return extension_match

    twice_decoded = unquote(once_decoded)
    extension_match = _match_extension(twice_decoded)
    if extension_match is not None:
        return extension_match

    return ".bin"


def build_image_file_name(image_url: str, image_index: int) -> str:
    image_hash = hashlib.md5(image_url.encode("utf-8"), usedforsecurity=False).hexdigest()[:12]
    extension = infer_image_extension(image_url)
    return f"{image_index:03d}-{image_hash}{extension}"


def _match_extension(image_url: str) -> str | None:
    match = IMAGE_EXTENSION_PATTERN.search(image_url)
    if match is None:
        return None

    return f".{match.group(1).lower()}"

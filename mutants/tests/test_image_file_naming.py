from __future__ import annotations

import unittest

from substack_sync.image_file_naming import build_image_file_name, infer_image_extension


class ImageFileNamingTests(unittest.TestCase):
    def test_infer_image_extension_from_direct_image_url(self) -> None:
        extension = infer_image_extension("https://example.com/image/photo.PNG?size=large")

        self.assertEqual(extension, ".png")

    def test_infer_image_extension_from_encoded_substack_cdn_url(self) -> None:
        extension = infer_image_extension(
            "https://substackcdn.com/image/fetch/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fexample_2816x1536.jpeg"
        )

        self.assertEqual(extension, ".jpeg")

    def test_infer_image_extension_uses_binary_fallback_when_missing(self) -> None:
        extension = infer_image_extension("https://example.com/asset/no-extension")

        self.assertEqual(extension, ".bin")

    def test_build_image_file_name_is_deterministic_with_index_and_hash(self) -> None:
        file_name = build_image_file_name(
            image_url="https://example.com/asset/photo.png",
            image_index=3,
        )

        self.assertEqual(file_name, "003-ae566d383274.png")


if __name__ == "__main__":
    unittest.main()

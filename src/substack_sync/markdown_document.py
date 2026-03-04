from __future__ import annotations

from dataclasses import dataclass

from substack_sync.empty_markdown_error import EmptyMarkdownError


@dataclass(frozen=True)
class MarkdownDocument:
    content: str

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise EmptyMarkdownError("Markdown content is empty.")

    @classmethod
    def from_raw_text(cls, raw_markdown: str) -> MarkdownDocument:
        normalized_markdown = raw_markdown if raw_markdown.endswith("\n") else f"{raw_markdown}\n"
        return cls(content=normalized_markdown)

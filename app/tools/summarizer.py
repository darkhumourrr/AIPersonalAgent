"""Lightweight summarizer tool for Step 2.

This is a deterministic fallback summarizer used before LLM wiring in later steps.
"""

from __future__ import annotations

import re

from app.models.schemas import SummarizeInput, SummarizeResult

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?。！？])\s+")


def summarize_text(input_data: SummarizeInput) -> SummarizeResult:
    """Create a concise summary by selecting first N sentences."""

    normalized_text = " ".join(input_data.text.split())
    candidates = [s.strip() for s in _SENTENCE_SPLIT.split(normalized_text) if s.strip()]
    if not candidates:
        candidates = [normalized_text]

    selected = candidates[: input_data.max_sentences]

    if input_data.style == "bullet":
        summary = "\n".join(f"- {sentence}" for sentence in selected)
    else:
        summary = " ".join(selected)

    if input_data.style == "formal" and not summary.startswith("Summary:"):
        summary = f"Summary: {summary}"

    return SummarizeResult(summary=summary, sentence_count=len(selected))

"""Core tool interfaces and orchestrator for Step 2."""

from __future__ import annotations

from dataclasses import dataclass

from app.models.schemas import (
    PDFReadInput,
    PDFReadResult,
    SendEmailInput,
    SendEmailResult,
    SummarizeInput,
    SummarizeResult,
)
from app.tools.email_sender import send_email
from app.tools.pdf_reader import read_document
from app.tools.summarizer import summarize_text


@dataclass(slots=True)
class CoreTools:
    """Convenience wrapper over the three core tools."""

    def read_pdf(self, payload: PDFReadInput) -> PDFReadResult:
        return read_document(payload)

    def summarize(self, payload: SummarizeInput) -> SummarizeResult:
        return summarize_text(payload)

    def send_email(self, payload: SendEmailInput) -> SendEmailResult:
        return send_email(payload)

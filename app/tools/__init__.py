"""Tool package exports."""

from app.tools.email_sender import send_email
from app.tools.interfaces import CoreTools
from app.tools.pdf_reader import PDFReadError, read_document
from app.tools.summarizer import summarize_text

__all__ = [
    "CoreTools",
    "PDFReadError",
    "read_document",
    "send_email",
    "summarize_text",
]

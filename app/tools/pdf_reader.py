"""Document reader tool implementation.

Supports PDF and plain text files. PDF extraction uses ``pypdf`` when available.
"""

from __future__ import annotations

from pathlib import Path

from app.models.schemas import PDFReadInput, PDFReadResult


class PDFReadError(RuntimeError):
    """Raised when document content cannot be extracted."""


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # pragma: no cover - depends on env package
        raise PDFReadError("pypdf is required to read PDF files.") from exc

    reader = PdfReader(str(path))
    text_parts = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(part.strip() for part in text_parts if part.strip())
    if not text:
        raise PDFReadError("No extractable text found in PDF.")
    return text


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def read_document(input_data: PDFReadInput) -> PDFReadResult:
    """Read text from local PDF/TXT and return normalized result."""

    path = Path(input_data.file_path)
    if not path.exists() or not path.is_file():
        raise PDFReadError(f"File not found: {input_data.file_path}")

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        text = _read_pdf(path)
    elif suffix in {".txt", ".md"}:
        text = _read_text(path)
    else:
        raise PDFReadError(f"Unsupported file type: {suffix}")

    text = text[: input_data.max_chars].strip()
    return PDFReadResult(file_path=str(path), text=text, char_count=len(text))

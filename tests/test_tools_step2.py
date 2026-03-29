from pathlib import Path

from app.models.schemas import PDFReadInput, SendEmailInput, SummarizeInput
from app.tools.email_sender import send_email
from app.tools.pdf_reader import read_document
from app.tools.summarizer import summarize_text


def test_read_document_txt(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text("第一句。第二句。第三句。", encoding="utf-8")

    result = read_document(PDFReadInput(file_path=str(file_path), max_chars=2000))

    assert result.char_count > 0
    assert "第一句" in result.text


def test_summarize_text_bullet_style() -> None:
    result = summarize_text(
        SummarizeInput(
            text="Sentence one. Sentence two. Sentence three.",
            max_sentences=2,
            style="bullet",
        )
    )

    assert result.sentence_count == 2
    assert result.summary.startswith("- Sentence one.")


def test_send_email_dry_run() -> None:
    result = send_email(
        SendEmailInput(
            to="demo@example.com",
            subject="Weekly Summary",
            body="Here is your summary",
            dry_run=True,
        )
    )

    assert result.status == "dry_run"
    assert result.provider == "mock"
    assert result.message_id.startswith("msg_")

"""Regression tests ensuring Step 1 scaffold and Step 2 tools stay compatible."""

from app.models.schemas import PDFReadInput, SendEmailInput, SummarizeInput
from app.tools.interfaces import CoreTools


def test_core_tools_wrapper_wires_step2_components(tmp_path) -> None:
    tools = CoreTools()

    sample = tmp_path / "compatibility.txt"
    sample.write_text("Alpha. Beta. Gamma.", encoding="utf-8")

    read_result = tools.read_pdf(PDFReadInput(file_path=str(sample), max_chars=1000))
    summary_result = tools.summarize(
        SummarizeInput(text=read_result.text, max_sentences=2, style="concise")
    )
    mail_result = tools.send_email(
        SendEmailInput(
            to="compat@example.com",
            subject="Compatibility Test",
            body=summary_result.summary,
            dry_run=True,
        )
    )

    assert "Alpha" in read_result.text
    assert summary_result.sentence_count == 2
    assert mail_result.status == "dry_run"

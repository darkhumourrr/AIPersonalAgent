"""Pydantic schemas for Step 2 core tools and task planning payloads."""

from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class TaskType(str, Enum):
    """Supported high-level task categories."""

    SUMMARIZE_PDF = "summarize_pdf"
    SEND_EMAIL = "send_email"


class PlanStep(BaseModel):
    """A single executable step in the task plan."""

    step_id: str = Field(..., description="Unique step id, e.g. step_1")
    task_type: TaskType
    description: str = Field(..., min_length=3)
    depends_on: list[str] = Field(default_factory=list)


class TaskPlan(BaseModel):
    """Structured task plan returned by planner nodes."""

    user_request: str = Field(..., min_length=3)
    steps: list[PlanStep] = Field(default_factory=list)


class PDFReadInput(BaseModel):
    """Input schema for PDF/document text extraction tool."""

    file_path: str = Field(..., description="Local file path")
    max_chars: int = Field(default=30_000, ge=500, le=200_000)


class PDFReadResult(BaseModel):
    """Output schema for PDF/document extraction."""

    file_path: str
    text: str
    char_count: int = Field(..., ge=0)


class SummarizeInput(BaseModel):
    """Input schema for summarization tool."""

    text: str = Field(..., min_length=1)
    max_sentences: int = Field(default=5, ge=1, le=12)
    style: Literal["concise", "formal", "bullet"] = "concise"


class SummarizeResult(BaseModel):
    """Output schema for summarization tool."""

    summary: str
    sentence_count: int = Field(..., ge=1)


class SendEmailInput(BaseModel):
    """Input schema for email sender tool."""

    to: EmailStr
    subject: str = Field(..., min_length=1, max_length=180)
    body: str = Field(..., min_length=1)
    dry_run: bool = True


class SendEmailResult(BaseModel):
    """Output schema for email sender tool."""

    status: Literal["sent", "dry_run"]
    message_id: str
    provider: str = "mock"

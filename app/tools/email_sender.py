"""Email sender tool (mock implementation for Step 2)."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from app.models.schemas import SendEmailInput, SendEmailResult


def send_email(input_data: SendEmailInput) -> SendEmailResult:
    """Send email or simulate sending based on dry_run flag."""

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    message_id = f"msg_{timestamp}_{uuid4().hex[:10]}"
    status = "dry_run" if input_data.dry_run else "sent"
    return SendEmailResult(status=status, message_id=message_id, provider="mock")

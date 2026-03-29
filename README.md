# AI Personal Agent

Autonomous Task Agent for the workflow:

> "帮我总结这个 PDF + 发邮件"

## Current status

This repository now contains:

- ✅ Step 1: FastAPI scaffold and project layout
- ✅ Step 2: Core tools + structured data models

## Step 2 implementation details

### Core tools

- `read_document` (PDF/TXT reader)
  - supports `.pdf` via `pypdf`
  - supports `.txt/.md` for local testing
- `summarize_text`
  - deterministic sentence-based summarizer
  - supports `concise / formal / bullet` styles
- `send_email`
  - mock email sender
  - returns `message_id` and `status` (`sent` or `dry_run`)

### Data models (`app/models/schemas.py`)

- Task planning: `TaskType`, `PlanStep`, `TaskPlan`
- Tool IO models:
  - `PDFReadInput`, `PDFReadResult`
  - `SummarizeInput`, `SummarizeResult`
  - `SendEmailInput`, `SendEmailResult`


## Merge consistency note

To avoid Step 1/Step 2 PR conflicts, this branch keeps Step 2 as an additive layer on top of Step 1:

- Step 1 APIs (`/` and `/health`) remain unchanged
- Step 2 introduces tools and schemas without breaking Step 1 endpoints
- A dedicated compatibility test verifies wrapper integration across both steps

## Planned next steps

3. Build LangGraph workflow (planning + tool calling)
4. Add `/run_task` API for end-to-end execution
5. Add memory and error handling
6. Add tests and complete documentation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest -q
```

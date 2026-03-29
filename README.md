# AI Personal Agent

Autonomous Task Agent skeleton for the workflow:

> "帮我总结这个 PDF + 发邮件"

## Current status

This repository currently contains **Step 1 (project scaffold)**:

- FastAPI app bootstrap
- Initial package structure for agent/tools/memory/models/api
- Placeholder modules for upcoming implementation
- Basic health check test

## Planned implementation steps

1. Initialize project scaffold ✅
2. Implement core tools (PDF reader / summarizer / email sender)
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

Run test:

```bash
pytest -q
```

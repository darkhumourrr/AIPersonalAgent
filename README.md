# AI Personal Agent



> "帮我总结这个 PDF + 发邮件"

## Current status


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



```bash
pytest -q
```

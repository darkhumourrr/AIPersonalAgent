"""API routes for the project (skeleton)."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index() -> dict[str, str]:
    return {"message": "AI Personal Agent scaffold is ready"}

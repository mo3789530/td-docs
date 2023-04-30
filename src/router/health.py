from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter(tags=["health"])


class Health(BaseModel):
    status : str
    def __init__(self, status: str):
        self.status = status

@router.get("/health")
async def health() -> Health:
    return Health(status="up")

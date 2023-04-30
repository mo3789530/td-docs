from fastapi import APIRouter
from pydantic import BaseModel
import os
from src.libs.s3 import get_list_objects, get_object_by_key

router = APIRouter(tags=["tf-state"])


class StateObjects(BaseModel):
    status: str
    objects: list[str]
    def __init__(self, status: str, objects: list[str], **data) -> None:
        self.status = status
        self.objects = object
        super().__init__(**data)

@router.get("/state")
async def get_state_list() -> StateObjects:
    bucket = os.getenv("TF_STATE_BUCKET", "")
    objects = get_list_objects(bucket)
    return StateObjects("success", objects)

@router.get("/state/{key}")
async def get_state_object(key: str, format: str = "html") -> StateObjects:
    bucket = os.getenv("TF_STATE_BUCKET", "")
    object = get_object_by_key(bucket_name=bucket, key=key)
    
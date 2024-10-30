# api.py
from fastapi import APIRouter, Depends
from fastapi.security import APIKeyHeader

from .model import Thread, Message
from .service import create_thread, submit_message

router = APIRouter()

header_scheme = APIKeyHeader(name="SESSION")


@router.post("/v1/threads", response_model=Thread, tags=["threads-v1"], dependencies=[Depends(header_scheme)])
async def create_thread_endpoint():
    return create_thread()


@router.post("/v1/threads/{id}/messages", response_model=Message, tags=["threads-v1"],
             dependencies=[Depends(header_scheme)])
async def talk(id: str, message: Message) -> Message:
    return submit_message(id, message.content)

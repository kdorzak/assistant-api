# api.py
from fastapi import APIRouter

from .model import Thread, Message
from .service import create_thread, submit_message

router = APIRouter()


@router.post("/threads", response_model=Thread)
async def create_thread_endpoint():
    return create_thread()


@router.post("/threads/{id}/messages", response_model=Message)
async def talk(id: str, message: Message) -> Message:
    return submit_message(id, message.content)

# api.py
from fastapi import APIRouter
from fastapi import HTTPException

from .model import Thread, Message
from .service import create_thread, get_thread, add_message_to_thread

router = APIRouter()


@router.post("/threads", response_model=Thread)
async def create_thread_endpoint():
    return create_thread()


@router.post("/threads/{id}/messages", response_model=Thread)
async def add_message_to_thread_endpoint(id2: int, message: Message) -> Thread:
    thread = add_message_to_thread(id2, message.content)
    if thread is None:
        raise HTTPException(status_code=404, detail="Thread not found")
    return thread

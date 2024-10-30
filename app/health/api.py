# api.py
from fastapi import APIRouter

from .model import Health

router = APIRouter()

@router.get("/actuator/health", response_model=Health)
async def create_thread_endpoint():
    return Health(
        status="UP"
    )

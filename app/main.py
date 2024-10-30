# main.py
from fastapi import FastAPI

from app.thread import api as thread_router
from app.health import api as health_router

app = FastAPI()

app.include_router(thread_router.router)
app.include_router(health_router.router)

# models.py
from pydantic import BaseModel


class Thread(BaseModel):
    id: str


class Message(BaseModel):
    content: str

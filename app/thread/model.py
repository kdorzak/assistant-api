# models.py
from pydantic import BaseModel
from typing import List

class Thread(BaseModel):
    id: int
    messages: List[str]

class Message(BaseModel):
    content: str
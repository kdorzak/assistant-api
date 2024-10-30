from openai import OpenAI
from app.config import settings


client = OpenAI(
    api_key=settings.open_api_key,
)

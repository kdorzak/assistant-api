# main.py
import uvicorn
from fastapi import FastAPI

from thread import api as thread_router

app = FastAPI()

app.include_router(thread_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

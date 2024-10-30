# Successfully creates a new thread with a unique ID
from fastapi.testclient import TestClient

from app.thread.service import threads
from app.thread.api import router

client = TestClient(router)


def test_create_thread_success():
    response = client.post("/threads")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] in threads
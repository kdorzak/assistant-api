# services.py
import logging
import time

from app.agent.client import client
from app.agent.setup import current_assistant
from .model import Thread, Message

logger = logging.getLogger(__name__)


def wait_on_run(run, thread_id):
    loop_count = 0
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        loop_count += 1
        time.sleep(0.01)
    logger.info(f"Got response after {loop_count} tries")
    return run


def create_thread() -> Thread:
    thread = client.beta.threads.create()
    return Thread(id=thread.id, messages=[])


def submit_message(thread_id: str, message: str) -> Message:
    thread = client.beta.threads.retrieve(thread_id)

    client.beta.threads.messages.create(
        thread.id,
        role="user",
        content=message,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id, assistant_id=current_assistant.id
    )
    wait_on_run(run, thread_id)

    last_message = client.beta.threads.messages.list(
        thread_id=thread_id,
        limit=1,
    ).data[0]
    response = "".join(
        entry.text.value for entry in last_message.content if entry.type == "text"
    )

    return Message(content=response)

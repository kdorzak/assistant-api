# services.py
from typing import List, Dict
from .model import Thread

# In-memory storage for threads and messages
threads: Dict[int, List[str]] = {}
thread_counter = 0

def create_thread() -> Thread:
    global thread_counter
    thread_counter += 1
    threads[thread_counter] = []
    return Thread(id=thread_counter, messages=[])

def get_thread(id: int) -> Thread :
    if id not in threads:
        return None
    return Thread(id=id, messages=threads[id])

def add_message_to_thread(id: int, message_content: str) -> Thread:
    if id not in threads:
        return None
    threads[id].append(message_content)
    return Thread(id=id, messages=threads[id])
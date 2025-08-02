import asyncio
from collections import defaultdict


class StreamManager:
    """Manage per-session asyncio queues for server-sent events."""

    def __init__(self) -> None:
        self._queues: defaultdict[int, asyncio.Queue[str]] = defaultdict(asyncio.Queue)

    def get_queue(self, session_id: int) -> asyncio.Queue:
        return self._queues[session_id]


stream_manager = StreamManager()

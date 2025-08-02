from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from .message import Message


class Session(BaseModel):
    id: int
    created_at: datetime
    status: str
    messages: List[Message] = []

    model_config = ConfigDict(from_attributes=True)


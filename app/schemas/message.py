from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MessageBase(BaseModel):
    content: str
    type: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


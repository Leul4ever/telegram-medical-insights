from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageBase(BaseModel):
    message_id: int
    channel_name: str
    message_text: Optional[str] = None
    message_date: datetime
    view_count: int
    forward_count: int

class Message(MessageBase):
    class Config:
        orm_mode = True

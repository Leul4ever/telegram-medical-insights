from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class ProductMention(BaseModel):
    term: str
    count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_date: datetime
    message_text: Optional[str]
    view_count: Optional[int]

class VisualContentStat(BaseModel):
    channel_name: str
    image_count: int
    promotional_count: int
    category_distribution: dict

class StandardResponse(BaseModel):
    status: str
    data: Any

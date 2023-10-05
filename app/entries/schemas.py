from datetime import datetime

from pydantic import BaseModel

from app.emotions.schemas import EmotionsSchema


class EntrySchema(BaseModel):
    user_id: int
    date: datetime
    situation: str
    thoughts_at_moment: str
    reaction: str
    helped_thoughts: str
    emotions: list[EmotionsSchema]
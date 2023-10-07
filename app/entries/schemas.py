from datetime import datetime

from pydantic import BaseModel

from app.emotions.schemas import EmotionsResponseSchema, EmotionsSchema


class EntrySchema(BaseModel):
    date: datetime
    situation: str
    thoughts_at_moment: str
    reaction: str
    helped_thoughts: str
    emotions: list[EmotionsSchema]


class EntryResponseSchema(BaseModel):
    id: int
    user_id: int
    date: datetime
    situation: str
    thoughts_at_moment: str
    reaction: str
    helped_thoughts: str
    emotions: list[EmotionsResponseSchema]


class EntryIdSchema(BaseModel):
    id: int

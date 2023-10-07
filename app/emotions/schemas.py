from pydantic import BaseModel

from app.emotions.models import EmotionsEnum


class EmotionsSchema(BaseModel):
    emotion: str
    rate_at_moment: int
    rate_after: int


class EmotionsResponseSchema(BaseModel):
    id: int
    entry_id: int
    emotion: EmotionsEnum
    rate_at_moment: int
    rate_after: int

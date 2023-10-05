from pydantic import BaseModel


class EmotionsSchema(BaseModel):
    emotion_name: str
    rate_at_moment: int
    rate_after: int

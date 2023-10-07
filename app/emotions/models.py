import enum

from sqlalchemy import CheckConstraint, Column, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class EmotionsEnum(enum.Enum):
    IRRITATION = "irritation"
    ANGER = "anger"
    RAGE = "rage"
    FURY = "fury"
    EXCITEMENT = "excitement"
    ANXIETY = "anxiety"
    FEAR = "fear"
    HORROR = "horror"
    SADNESS = "sadness"
    MELANCHOLY = "melancholy"
    SORROW = "sorrow"
    YEARNING = "yearning"
    DESPAIR = "despair"
    GRIEF = "grief"
    EMBARRASSMENT = "embarrassment"
    SHAME = "shame"
    GUILT = "guilt"
    JEALOUSY = "jealousy"
    ENVY = "envy"
    RESENTMENT = "resentment"
    DISAPPOINTMENT = "disappointment"
    INDIGNATION = "indignation"
    CONTEMPT = "contempt"
    DISGUST = "disgust"
    HATRED = "hatred"


class Emotions(Base):
    __tablename__ = "emotions"
    __table_args__ = (
        CheckConstraint(
            "(rate_at_moment > 0 AND rate_at_moment <= 10) AND (rate_after > 0 AND rate_after <= 10)"
        ),
    )

    id = Column(Integer, primary_key=True, nullable=False)
    entry_id = Column(ForeignKey("entries.id", ondelete="CASCADE"), nullable=False)
    emotion = Column(Enum(EmotionsEnum), nullable=False)
    rate_at_moment = Column(Integer, nullable=False)
    rate_after = Column(Integer, nullable=False)

    entry = relationship("Entries", back_populates="emotions")

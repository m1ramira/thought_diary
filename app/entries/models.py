from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Entries(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey("users.user_id"), nullable=False)
    date = Column(DateTime, nullable=False)
    situation = Column(String, nullable=False)
    thoughts_at_moment = Column(String, nullable=False)
    reaction = Column(String, nullable=False)
    helped_thoughts = Column(String, nullable=False)

    user = relationship("Users", backref="entries", lazy=True)
    emotions = relationship("Emotions", back_populates="entry", cascade="all,delete")

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    email = Column(String)

    def __str__(self):
        return f"User {self.username}"


class SUsers(BaseModel):
    id: int
    username: str
    hashed_password: str
    email: str

    class Config:
        orm_model = True

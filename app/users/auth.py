from datetime import datetime, timedelta
from typing import Any, Optional

from jose import jwt
from passlib.context import CryptContext

from app.config import settings
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        settings.ALGORITHM,
    )

    return encoded_jwt


async def auth_user(username: str, password: str) -> Optional[Any]:
    user = await UsersDAO.find_one_or_none(username=username)

    if user is None or not verify_password(password, user.hashed_password):
        return None

    return user

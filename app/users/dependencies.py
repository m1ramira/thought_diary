from datetime import datetime
from typing import Any, Optional

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.users.dao import UsersDAO
from app.users.exceptions import (IncorrectTokenFormatException,
                                  TokenAbsentException, TokenExpiredException,
                                  UserIsNotFoundException)


def get_token(request: Request) -> str:
    """
    Get access token from cookie.
    :param request: Request
    :return: str
    """
    token = request.cookies.get("access_token")

    if not token:
        raise TokenAbsentException

    return token


async def get_current_user(token: str = Depends(get_token)) -> Optional[Any]:
    """
    Get current user by user_id.
    Raise exception, if token is incorrect, or session is expired, or user is not in DB.
    :param token: str
    :return: User or Exception
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            settings.ALGORITHM,
        )
    except JWTError:
        raise IncorrectTokenFormatException

    expire_time = payload.get("exp")
    if not expire_time or int(expire_time) < datetime.utcnow().timestamp():
        raise TokenExpiredException

    user_id = payload.get("user_id")
    if not user_id:
        raise UserIsNotFoundException

    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotFoundException

    return user

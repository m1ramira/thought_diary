from fastapi import APIRouter, Response

from app.users.auth import auth_user, create_access_token, get_password_hash
from app.users.dao import UsersDAO
from app.users.exceptions import (IncorrectEmailOrPasswordException,
                                  UserAlreadyExistsException)
from app.users.schemas import UserAuthSchema

router = APIRouter(
    prefix="/auth",
    tags=["Authentication and Users"]
)


@router.post("/register")
async def register(user_data: UserAuthSchema) -> None:
    """
    Function to register user.
    :param user_data:

    :return: None
    """
    existing_user = await UsersDAO.find_one_or_none(username=user_data.username)
    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        username=user_data.username,
        hashed_password=hashed_password,
    )


@router.post("/login")
async def login(response: Response, user_data: UserAuthSchema) -> str:
    """
    Function to log in user.
    :param response: Response
    :param user_data: SUsersAuth
    :return: str
    """
    user = await auth_user(user_data.username, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException

    access_token = create_access_token({"user_id": str(user.user_id)})
    response.set_cookie("access_token", access_token, httponly=True)

    return access_token


@router.post("/logout")
async def logout(response: Response) -> None:
    """
    Function to log out user.
    :param response: Response
    :return:
    """
    response.delete_cookie("access_token")

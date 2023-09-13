from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def find_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id=user_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()

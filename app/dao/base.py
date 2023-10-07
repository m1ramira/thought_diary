from fastapi import HTTPException, status
from sqlalchemy import delete, insert, select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **kwargs: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)

            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **kwargs: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)

            return result.scalars().all()

    @classmethod
    async def add(cls, **kwargs: str) -> None:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **kwargs: str) -> None:
        async with async_session_maker() as session:
            query = (
                delete(cls.model)
                .filter_by(**kwargs)
                .returning(cls.model.__table__.c.id)
            )
            deleted_entry = await session.execute(query)
            await session.commit()

            result = deleted_entry.scalar()
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Missing resource.",
                )

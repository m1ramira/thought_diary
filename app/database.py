from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    pass


if settings.MODE == "DEV":
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}
elif settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
elif settings.MODE == "PROD":
    DATABASE_URL = settings.PROD_DATABASE_URL
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

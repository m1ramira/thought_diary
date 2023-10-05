import asyncio
import json

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker, engine
from app.main import app as fastapi_app
from app.users.models import Users


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    users = open_mock_json("users")

    async with async_session_maker() as session:
        add_user = insert(Users).values(users)

        await session.execute(add_user)
        await session.commit()


@pytest_asyncio.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(ac: AsyncClient):
    data = {
        "username": "auth_client",
        "password": "hashed_password",
    }
    await ac.post("/auth/register", json=data)
    await ac.post("/auth/login", json=data)
    yield ac

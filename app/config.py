from typing import Literal

from dotenv import load_dotenv
from pydantic import root_validator
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """DB settings"""
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    PROD_DB_HOST: str
    PROD_DB_PORT: int
    PROD_DB_USER: str
    PROD_DB_PASS: str
    PROD_DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    @root_validator(pre=False, skip_on_failure=True)
    def get_db_url(cls, val: dict) -> dict:
        """Create DB_URL and add to all parameters.
        :type val: dict
        """
        val['DATABASE_URL'] = (f"postgresql+asyncpg://{val['DB_USER']}:{val['DB_PASS']}@"
                               f"{val['DB_HOST']}:{val['DB_PORT']}/{val['DB_NAME']}")

        val['TEST_DATABASE_URL'] = (f"postgresql+asyncpg://{val['TEST_DB_USER']}:{val['TEST_DB_PASS']}@"
                                    f"{val['TEST_DB_HOST']}:{val['TEST_DB_PORT']}/{val['TEST_DB_NAME']}")

        val['PROD_DATABASE_URL'] = (f"postgresql+asyncpg://{val['PROD_DB_USER']}:{val['PROD_DB_PASS']}@"
                                    f"{val['PROD_DB_HOST']}:{val['PROD_DB_PORT']}/{val['PROD_DB_NAME']}")

        return val

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

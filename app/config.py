from pydantic import root_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    """DB settings"""
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    @root_validator(pre=False, skip_on_failure=True)
    def get_db_url(cls, val: dict) -> dict:
        """Create DB_URL and add to all parameters.
        :type val: dict
        """
        val['DATABASE_URL'] = (f"postgresql+asyncpg://{val['DB_USER']}:{val['DB_PASS']}@"
                         f"{val['DB_HOST']}:{val['DB_PORT']}")

        return val

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

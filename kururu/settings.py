from secrets import token_hex

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class SessionSettings(BaseSettings):
    SESSION_SECRET_KEY: str


class DatabaseSettings(BaseSettings):
    DATABASE_DRIVER: str
    DATABASE_DIALECT: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str


class JWTSettings(BaseSettings):
    JWT_ACCESS_TOKEN_SECRET_KEY: str = Field(default=token_hex(256))
    JWT_REFRESH_TOKEN_SECRET_KEY: str = Field(default=token_hex(256))
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=180)
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(default=180)

from settings import Settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

settings = Settings()

ENGINE = create_async_engine(settings.database_uri)


def get_async_session_maker():
    return async_sessionmaker(ENGINE)

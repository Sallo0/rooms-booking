from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

DB_URL = settings.DB_URL
DB_PARAMS = {"echo": True, "future": True}

if settings.MODE == "test":
    DB_URL = settings.TEST_DB_URL
    DB_PARAMS = {"poolclass": NullPool}

engine = create_async_engine(DB_URL, **DB_PARAMS)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass

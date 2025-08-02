from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config.config import get_settings

config = get_settings()

engine = create_async_engine(config.database.url, echo=config.database.echo)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
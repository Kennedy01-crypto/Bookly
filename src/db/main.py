from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.books.models import Book


engine = AsyncEngine(create_engine(Config.DATABASE_URL, echo=True, future=True))

# initialize db connection
async def init_db():
    async with engine.begin() as conn:
       await conn.run_sync(SQLModel.metadata.create_all)
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):

    print(f"Server is starting up...")
    await init_db()
    yield #separate the two
    print(f"Server is shutting down...")

version= "v1"

app = FastAPI(
    lifespan=life_span,
    version=version,
    title="Bookly API",
    description="This is a simple API for managing books",
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])

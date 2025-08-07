from fastapi import FastAPI
from src.books.routes import book_router

version= "v1"

app = FastAPI(
    version=version,
    title="Bookly API",
    description="This is a simple API for managing books",
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])

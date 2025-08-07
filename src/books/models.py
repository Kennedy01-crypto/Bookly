from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID
import uuid


class Book(SQLModel, table=True):
    __tablename__ = "books"  # type: ignore 

    uuid: UUID = Field(sa_column=Column(
        pg.UUID,
        nullable=False,
        primary_key=True,
        default=uuid.uuid4(),
        unique=True
    ))
    title: str
    author: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field( 
        sa_column=Column(pg.TIMESTAMP,default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP,default=datetime.now, onupdate=datetime.now)
    )

    def __repr__(self):
        return f"<Book {self.title}>"
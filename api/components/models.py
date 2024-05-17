from sqlalchemy import Column, Integer, String
from api.core.data_base import Base


class Book(Base):
    """
    SQLAlchemy model for the 'books' table.

    Attributes:
        id (int): Primary key for the table.
        isbn_10 (str): ISBN-10 of the book, unique and indexed.
        isbn_13 (str): ISBN-13 of the book, unique and indexed.
        title (str): Title of the book, indexed.
        author (str): Author of the book, indexed.
        summary (str): Summary of the book.
        cover_url (str): URL of the book's cover image.
    """
    __tablename__ = "books"
    id = Column(Integer(), primary_key=True, index=True)
    isbn_10 = Column(String(10), unique=True, index=True)
    isbn_13 = Column(String(13), unique=True, index=True)
    title = Column(String(64), index=True)
    author = Column(String(320), index=True)
    summary = Column(String(320))
    cover_url = Column(String(320))

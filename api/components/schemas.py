from pydantic import BaseModel, root_validator
from typing import Optional


class BookISBN(BaseModel):
    """
    Pydantic model for representing an ISBN input.

    Attributes:
        isbn (str): The ISBN of the book.
    """
    isbn: str


class BookCreate(BaseModel):
    """
    Pydantic model for creating a book record.

    Attributes:
        isbn_10 (Optional[str]): The ISBN-10 of the book.
        isbn_13 (Optional[str]): The ISBN-13 of the book.
        title (str): The title of the book.
        author (str): The author(s) of the book.
        summary (str): A summary of the book.
        cover_url (str): The URL of the book's cover image.
    """
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    title: str
    author: str
    summary: str
    cover_url: str


class Book(BookCreate):
    """
    Pydantic model for representing a book record with an ID.

    Attributes:
        id (int): The unique identifier of the book.
    """
    id: int

    class Config:
        from_attributes = True

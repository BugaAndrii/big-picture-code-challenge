from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api.components import schemas
from api.apps.services import library
from api.core.data_base import get_db
from api.core import crud

library_endpoint = APIRouter()


@library_endpoint.get("/isbn/{isbn}", response_model=schemas.BookCreate)
async def get_book_info(isbn: str) -> schemas.BookCreate:
    """
    Retrieve book information by ISBN.

    :param isbn: The ISBN of the book to retrieve.
    :return: Book details.
    :raises HTTPException: If the ISBN is invalid or the book is not found.
    """
    if not library.is_valid_isbn(isbn):
        raise HTTPException(status_code=400, detail="Invalid ISBN")
    book_info = await library.fetch_book_details(isbn)
    if not book_info:
        raise HTTPException(status_code=404, detail="Book not found")
    return schemas.BookCreate(**book_info)


@library_endpoint.post("/books", response_model=schemas.Book)
async def save_book(book: schemas.BookISBN, db: Session = Depends(get_db))->schemas.Book:
    """
    Save book details in the database.

    :param book: The book information to save.
    :param db: The database session dependency.
    :return: The saved book details.
    :raises HTTPException: If the ISBN is invalid or the book is already registered.
    """
    if not library.is_valid_isbn(book.isbn):
        raise HTTPException(status_code=400, detail="Invalid ISBN")
    db_book = crud.get_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already registered")
    book_info = await library.fetch_book_details(book.isbn)
    if not book_info:
        raise HTTPException(status_code=404, detail="Book not found")
    book_create = schemas.BookCreate(**book_info)
    return crud.create_book(db=db, book=book_create)


@library_endpoint.get("/books", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of books from the database.

    :param skip: The number of records to skip (default is 0).
    :param limit: The maximum number of records to return (default is 100).
    :param db: The database session dependency.
    :return: A list of books.
    """
    return crud.get_books(db=db, skip=skip, limit=limit)

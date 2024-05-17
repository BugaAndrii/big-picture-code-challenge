from sqlalchemy.orm import Session

from api.components import models, schemas


def get_book_by_isbn(db: Session, isbn: str):
    """
    Retrieve a book from the database by its ISBN.

    :param db: Database session.
    :param isbn: ISBN of the book to retrieve.
    :return: The book object if found, otherwise None.
    """
    if len(isbn) == 10:
        return db.query(models.Book).filter(models.Book.isbn_10 == isbn).first()
    else:
        return db.query(models.Book).filter(models.Book.isbn_13 == isbn).first()


def create_book(db: Session, book: schemas.BookCreate):
    """
    Create a new book record in the database.

    :param db: Database session.
    :param book: Book data to create a new record.
    :return: The newly created book object.
    """
    book_data = models.Book(**book.dict())
    db.add(book_data)
    db.commit()
    db.refresh(book_data)
    return book_data


def get_books(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of books from the database with pagination.

    :param db: Database session.
    :param skip: Number of records to skip (default is 0).
    :param limit: Maximum number of records to return (default is 100).
    :return: A list of book objects.
    """
    return db.query(models.Book).offset(skip).limit(limit).all()

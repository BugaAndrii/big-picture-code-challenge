import re
import aiohttp


def is_valid_isbn(isbn: str) -> bool:
    """
    Validate the given ISBN.

    :param isbn: The ISBN to validate.
    :return: True if the ISBN is valid, False otherwise.
    """
    isbn_10_regex = r"^\d{9}(\d|X)$"  # Regular expression for validating ISBN-10
    isbn_13_regex = r"^(97(8|9))?\d{9}(\d|X)$"  # Regular expression for validating ISBN-13
    return re.match(isbn_10_regex, isbn) is not None or re.match(isbn_13_regex, isbn) is not None


async def fetch_book_details(isbn: str):
    """
    Fetch book details from the OpenLibrary API using the provided ISBN.

    :param isbn: The ISBN of the book to fetch details for.
    :return: A dictionary containing book details, or None if the book is not found.
    """
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            data = await response.json()
            book_key = f"ISBN:{isbn}"
            if book_key in data:
                book_data = data[book_key]
                # Extract and return the relevant book details
                return {
                    "title": book_data.get("title", "No Title"),
                    "author": ", ".join([author["name"] for author in book_data.get("authors", [])]),
                    "summary": book_data.get("notes", "No Summary"),
                    "cover_url": book_data.get("cover", {}).get("large", ""),
                    "isbn_10": book_data.get("identifiers", {}).get("isbn_10", [None])[0],
                    "isbn_13": book_data.get("identifiers", {}).get("isbn_13", [None])[0]
                }
    return None

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley"),
}


@app.get("/books")
def list_books():
    # TODO: Return every book in the catalog.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the requested book or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Add the book to the catalog and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Replace an existing book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove an existing book or raise HTTPException with status 404.
    pass

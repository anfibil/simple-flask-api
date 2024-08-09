from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sqlite3
import os


# Init app
app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    published: str
    first_sentence: str


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.get("/")
async def home():
    return "<h1>Distant Reading Archive</h1><p>This is a prototype API</p>"


@app.get("/api/v2/resources/books/all")
async def api_all():
    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return JSONResponse(content=all_books)


@app.get("/api/v2/resources/books")
async def api_filter(id: int = None, published: str = None, author: str = None):
    query = 'SELECT * FROM books WHERE'
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    
    if published:
        query += ' published=? AND'
        to_filter.append(published)

    if author:
        query += ' author=? AND'
        to_filter.append(author)

    if not(id or published or author):
        raise HTTPException(status_code=404, detail="The resource could not be found")

    query = query[:-4] + ';'

    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return JSONResponse(content=results)


@app.post("/api/v2/resources/books")
async def add_book(book: Book):
    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    query = f'INSERT INTO books (title, author, published, first_sentence) VALUES ("{book.title}", "{book.author}", "{book.published}", "{book.first_sentence}");'

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return JSONResponse(content=book.dict())


# A method that runs the application server.
# Note: FastAPI is typically run with a command like `uvicorn app:app --host 0.0.0.0 --port 5000`
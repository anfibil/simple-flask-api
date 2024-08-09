from fastapi import FastAPI, HTTPException, Query
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

# A route to return the home page
@app.get("/")
def home():
    return "<h1>Distant Reading Archive</h1><p>This is a prototype API</p>"

# A route to return all available entries in our catalog.
@app.get("/api/v2/resources/books/all")
def api_all():
    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    return JSONResponse(content=[dict(row) for row in all_books])

@app.get("/api/v2/resources/books")
def api_filter(id: int = Query(None), published: str = Query(None), author: str = Query(None)):
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

    if not (id or published or author):
        raise HTTPException(status_code=404, detail="The resource could not be found")

    query = query[:-4] + ';'

    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    return JSONResponse(content=[dict(row) for row in results])

@app.post("/api/v2/resources/books")
def add_book(book: Book):
    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    query = f'INSERT INTO books (title, author, published, first_sentence) VALUES (?, ?, ?, ?);'
    cur = conn.cursor()
    cur.execute(query, (book.title, book.author, book.published, book.first_sentence))
    conn.commit()
    return book

# A method that runs the application server.
# Note: Uvicorn will be used to run this FastAPI app instead of the built-in server.
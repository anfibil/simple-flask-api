from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

# Init app
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.get('/', response_class=HTMLResponse)
async def home():
    return "<h1>Distant Reading Archive</h1><p>This is a prototype API</p>"

@app.get('/api/v2/resources/books/all')
async def api_all():
    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return all_books

@app.get('/api/v2/resources/books')
async def api_filter(id: int = Query(None), published: str = Query(None), author: str = Query(None)):
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

    return results

@app.post('/api/v2/resources/books')
async def add_book(content: dict):
    if not content:
        raise HTTPException(status_code=400, detail="The content isn't of type JSON")

    title = content.get('title')
    author = content.get('author')
    published = content.get('published')
    first_sentence = content.get('first_sentence')

    db_path = os.path.join('db', 'books.db')    
    conn = sqlite3.connect(db_path)
    query = f'INSERT INTO books (title, author, published, first_sentence) VALUES ("{title}", "{author}", "{published}", "{first_sentence}");'

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return content

# A method that runs the application server.
# FastAPI automatically runs the server when using uvicorn.
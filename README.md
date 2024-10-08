# Simple FastAPI Application

This project presents a simple REST API with Python and FastAPI to retrieve book data from a Sqlite3 database.

### How to use

1. Clone this project
2. run ```pip install pipenv```
3. run ```pipenv install```
4. run ```uvicorn app:app --reload```

### API request examples:
To access the data, open the browser and access the API as the examples below.

Get all books:

``` http://127.0.0.1:8000/api/v2/resources/books/all```

Get books where the author is *Connie Willis*

```http://127.0.0.1:8000/api/v2/resources/books?author=Connie+Willis```

Get books published in 2010

``` http://127.0.0.1:8000/api/v2/resources/books?published=2010```

A running version of this API can be found [here](https://simplefastapi-cpatrickalves.herokuapp.com/).
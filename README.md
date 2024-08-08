# Simple Flask API

This project provides a simple REST API that retrieves book data from a Sqlite3 database using Python and Flask.

### How to Use

1. Clone this project
2. Run `pip install pipenv`
3. Run `pipenv install`
4. Run `python api.py`

### Example API Requests:
To access the data, open a browser and access the API as shown in the examples below.

Get all books:

``` http://127.0.0.1:5000/api/v2/resources/books/all```

Get books by author *Connie Willis*

```http://127.0.0.1:5000/api/v2/resources/books?author=Connie+Willis```

Get books published in 2010:

``` http://127.0.0.1:5000/api/v2/resources/books?published=2010```

The current version of this API can be found [here](https://simpleflaskapi-cpatrickalves.herokuapp.com/)
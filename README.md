# API Flask Simple

Este proyecto presenta una API REST simple con Python y Flask para recuperar datos de libros de una base de datos Sqlite3.

### Cómo usar

1. Clona este proyecto
2. ejecuta ```pip install pipenv```
3. ejecuta ```pipenv install```
4. ejecuta ```python api.py```

### Ejemplos de solicitudes a la API:
Para acceder a los datos, simplemente abre el navegador y accede a la API como en los ejemplos a continuación.

Obtener todos los libros:

``` http://127.0.0.1:5000/api/v2/resources/books/all```

Obtener libros donde el autor es *Connie Willis*

```http://127.0.0.1:5000/api/v2/resources/books?author=Connie+Willis```

Obtener libros publicados en 2010

``` http://127.0.0.1:5000/api/v2/resources/books?published=2010```

Una versión en funcionamiento de esta API se puede encontrar [aquí](https://simpleflaskapi-cpatrickalves.herokuapp.com/).
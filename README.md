# シンプルなFlask API

このプロジェクトは、PythonとFlaskを使用してSqlite3データベースから書籍データを取得するシンプルなREST APIを提供します。

### 使用方法

1. このプロジェクトをクローンします
2. ```pip install pipenv```を実行します
3. ```pipenv install```を実行します
4. ```python api.py```を実行します

### APIリクエストの例:
データにアクセスするには、ブラウザを開いて以下の例のようにAPIにアクセスします。

すべての書籍を取得:

``` http://127.0.0.1:5000/api/v2/resources/books/all```

著者が*Connie Willis*の書籍を取得:

```http://127.0.0.1:5000/api/v2/resources/books?author=Connie+Willis```

2010年に出版された書籍を取得:

``` http://127.0.0.1:5000/api/v2/resources/books?published=2010```

このAPIの実行中のバージョンは[こちら](https://simpleflaskapi-cpatrickalves.herokuapp.com/)で見つけることができます。
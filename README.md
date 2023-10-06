<h1>Тестовое задание</h1>
<hr>
<h2>Развертывание:</h2>
<ul>

<li>

`git clone`

</li>

<li>

`docker compose up --build`

</li>
</ul>

P.S. Файл с переменными окружениями для БД уже находится в репозитории

<h3>Зависимости в корневой директории в файле requirements.txt</a></h3>
**В проекте используется PostgreSQL**
**Версия Python: 3.11**
<hr>

<h3>Эндпоинты:</h3>
http://localhost:8000/api/v1/service/stores/ <br>
Method: 

`post`

<br>
Request: 

`{"mobile": String}`

<br>
Response: 

`[{"id": Number, "name": String},]`

<br>
http://localhost:8000/api/v1/service/visit/ <br>
Method: 

`post`

<br>
Request: 

`{"mobile": String, "store_id": Number, "latitude": Number(Float), "longitude": Number(Float)}`

<br>

Response:  

`{"id": Number, "datetime_visited": "date-time(%Y-%m-%d %H:%M:%S)"}`

<br>
<hr>

<h3>Запуск тестов: </h3>
Внутри контейнера:

`docker exec -it <имя контейнера> /bin/bash`

`./manage.py test`
<hr>

<h3>Установка фикстур: </h3>

Фикстуры включают себя данные суперпользователя, а также данные для созданных моделей в БД.

`./manage.py loaddata fixture.json`
<hr>
<h3>Вход в админку: </h3>

*username: root*<br>
*password: 1234*<br>
*email: root@example.com*<br>

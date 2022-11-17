# Проект mailganer
***
Проект рассылает html email списку пользователей из БД.
***

## Возможности.

* Рассылка html email списку пользователей.
* html шаблоны используют переменные.
* Отслеживается открытие писем с записью в логи и БД.
***

## Установка.
***
Клонировать репозиторий и перейти в него в командной строке.

```
git clone git@github.com:mvrogozov/mailganer.git
```

Cоздать и активировать виртуальное окружение.

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
В папке mailganer создать файл .env,
записать в него переменные окружения:
* EMAIL_HOST='email server'    например 'smtp.yandex.ru'
* EMAIL_PORT='email server port'    например  587
* EMAIL_PASSWORD='password for your email'
* EMAIL_USER='your email'
* DJANGO_SECRET_KEY='secret key for django'

Выполнить миграции:

```
python manage.py migrate
```
Запустить сервер redis.

Запустить celery:
```
python -m celery -A mailganer worker -l info
```

Запустить проект:

```
python manage.py runserver
```

Эндпоинт для запуска отправки:
```
/sender/send/
```
для задержки между отправками передать параметр 
```
timeout
```
со значением задержки в секундах


***
Автор:
* Рогозов Михаил
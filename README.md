# Django Hash Static

Django_hash_static - это Django-приложение, которое добавляет новый template tag ``hash_static`` для создания уникального отпечатка статического файла. Template tag вычисляет md5-хеш содержимого файла и добавляет к пути файла, например:

    <img src="{% hash_static "img/earth.png" %}">

и результат после рендера:

    <img src="/static/img/earth.png?hash=d9013eb3cf6e7c68a9e293c8b70907c9">

Хеш меняется после любого изменения содержимого файла, тем самым вынуждая браузеры старых посетителей сайта подгружать новые файлы с сервера, а не использовать кэшированные.

## Требования

1. Python 3.x
2. Django 2.x

## Установка

1. ```pip install git+https://github.com/SibdevPro/django-hash-static.git@1.0.1```
2. Добавить 'django_hash_static' в INSTALLED_APPS
3. Не забыть добавить STATIC_ROOT в settings.py

## Использование

1. Подключить template tag

```{% load hash_static %}```

2. Использовать как и static, пример:

```<img src="{% hash_static "img/earth.png" %}">```

## ВАЖНО

Хеш добавляется только при DEBUG=False

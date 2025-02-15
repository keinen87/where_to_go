# Карта Москвы

Карта с местами для посещения в Москве.

## Как запустить ?

- Скачать код проекта.

- Установить зависимости:

```console
pip install -r requirements.txt
```

- Запустить сервер:

```console
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по-умолчанию.

Доступны следущие переменные:

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — [Что такое ALLOWED_HOSTS](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-ALLOWED_HOSTS).

****

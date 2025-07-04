# Набор автотестов для REST API (yavshoke-api-tests)

## Описание

Этот проект содержит автотесты для проверки основных эндпоинтов REST API сервиса. Тесты написаны на Python с использованием модулей `pytest` и `requests`.

## Структура проекта

yavshoke-api-tests/
├── .gitignore
├── README.md
├── requirements.txt
└── tests/
    ├── config.py         # Базовый URL API
    ├── schemas.py        # Тестовые данные (email, пароль, токен)
    ├── test_exist.py     # Тесты для /exist
    ├── test_health.py    # Тесты для /health
    ├── test_login.py     # Тесты для /auth/login
    ├── test_me.py        # Тесты для /user/me
    ├── test_name.py      # Тесты для /user/name
    └── test_register.py  # Тесты для /auth/register


## Как запустить тесты

1. Установить зависимости:
    ```
    pip install -r requirements.txt
    ```

2. Перед запуском тестов убедиться, что в системе зарегистрирован пользователь:
    - email: `test@yandex.ru`
    - пароль: `string`
Для тестов логина и проверки существования пользователя.

3. Убедиться, что токен `VALID_TOKEN` актуален и соответствует пользователю `test@yandex.ru`. Для тестов /user/me.
Токен можно получить, залогинившись этим пользователем и скопировав значение access_token из ответа.

4. Запустить тесты командой:
    ```
    pytest
    ```

## Описание файлов

- **requirements.txt** — зависимости проекта (`pytest`, `requests`)
- **config.py** — базовый URL API (`BASE_URL`)
- **schemas.py** — тестовые данные: email, пароль, токен
- **test_*.py** — тесты для соответствующих эндпоинтов


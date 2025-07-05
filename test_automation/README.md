# API Автотесты для "Я в ШОКе"

## Описание
Всем привет, здесь содержится набор тестов для проверки REST API прод-сервера https://api.yavshok.ru  
Покрывает: регистрацию, авторизацию, профили, проверку "в ШОКе", а также состояние сервера.

## Важный нюанс
Если после переноса возникла проблема с запуском тестов на зарегистрированного пользователя, в localhost, необходимо через swagger зарегистрировать пользователя
со следующими данными:

{
    "email": "101010@mail.com"
    "password": 123456
    "age": 22
}

После данной процедуры тесты, связанные с использованием токен будут работать корректно.

## Запуск тестов

```bash
pip install -r requirements.txt
pytest
```

## Предварительные итоги тестирования:
```
============================================== short test summary info ==============================================
FAILED test_api_shok/test_register.py::test_password_nospace_insert - assert 200 == 422
FAILED test_api_shok/test_register.py::test_passwordwith_specialsymbols_insert - assert 422 == 200
FAILED test_api_shok/test_register.py::test_50symbols_lenght_email_insert - assert 422 == 200
=========================================== 3 failed, 28 passed in 1.05s ============================================
```
# api-client и запуск тестов

Python-клиент сгенерирован по схеме API с помощью [OpenAPI Generator](https://openapi-generator.tech):

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Требования

Python 3.9+

## Установка и использование

Убедитесь, что у вас установлен python

```sh
python3 --version
```

А также pip или pip3

```sh
pip --version
pip3 --version
```

Установите зависимости

```sh
pip install -r test-requirements.txt
```

или

```sh
pip3 install -r test-requirements.txt
```

Создайте `.env` файл и задайте в `API_BASE_URL` хост с API

```sh
cp .env.example .env
```

### Тесты

Выполните `pytest tests` для запусков тестов.

## Документация для API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_health**](docs/DefaultApi.md#get_health) | **GET** /health | 
*DefaultApi* | [**get_user_me**](docs/DefaultApi.md#get_user_me) | **GET** /user/me | Get current user data
*DefaultApi* | [**patch_user_name**](docs/DefaultApi.md#patch_user_name) | **PATCH** /user/name | Update user name
*DefaultApi* | [**post_auth_login**](docs/DefaultApi.md#post_auth_login) | **POST** /auth/login | Sign in the user
*DefaultApi* | [**post_auth_register**](docs/DefaultApi.md#post_auth_register) | **POST** /auth/register | Sign up the user
*DefaultApi* | [**post_exist**](docs/DefaultApi.md#post_exist) | **POST** /exist | Check if user exists


## Документация для моделей запроса и ответа

 - [AuthResponse](docs/AuthResponse.md)
 - [AuthResponseUser](docs/AuthResponseUser.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetUserMe200Response](docs/GetUserMe200Response.md)
 - [GetUserMe401Response](docs/GetUserMe401Response.md)
 - [PatchUserNameRequest](docs/PatchUserNameRequest.md)
 - [PostAuthLoginRequest](docs/PostAuthLoginRequest.md)
 - [PostAuthRegisterRequest](docs/PostAuthRegisterRequest.md)
 - [PostExist200Response](docs/PostExist200Response.md)
 - [PostExistRequest](docs/PostExistRequest.md)
 - [User](docs/User.md)

## Author
Татьяна Мантрова

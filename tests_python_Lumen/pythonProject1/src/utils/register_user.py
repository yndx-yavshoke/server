import requests
import config


def register_user(email:str, password:str, age:int):
    """
      Функиця для авторегистрации пользователя
      передаем почту, пароль и возраст
      Вызывается в [tests/conftest.py]
    """

    data = {
        "email": email,
        "password": password,
        "age": age
    }

    url = config.SERVICE_URL + "auth/register"
    response = requests.post(url=url, json=data)

    if response.status_code == 200:
        print("User register")
    else:
        print("Check this, there seems to be an issue — the user might already be registered.")


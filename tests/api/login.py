import requests 

from tests.variables.const import LOGIN_URL

# Отправка запроса на ручку
# Отправляются данные существующего пользователя
def login_exist_user():
    url = LOGIN_URL
    payload = {
        "email": "test@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    return response.json()

# Отправка запроса на ручку
# Отправляются данные несуществующего пользователя
def login_non_exist_user():
    url = LOGIN_URL
    payload = {
        "email": "imnotexistactually@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    return response.json()
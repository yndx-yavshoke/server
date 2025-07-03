import requests 

from tests.variables.const import EXIST_URL

# Отправка запроса на ручку
# Отправляются данные существующего пользователя
def exist_user():
    url = EXIST_URL
    payload = {
        "email": "test@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    return response.json()

# Отправка запроса на ручку
# Отправляются данные несуществующего пользователя
def non_exist_user():
    url = EXIST_URL
    payload = {
        "email": "imnotexistactually@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    return response.json()
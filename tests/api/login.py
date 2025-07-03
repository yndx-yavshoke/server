import requests 

from tests.variables.const import LOGIN_URL

# Отправка запроса на ручку
# Отправляются данные существующего пользователя
def login():
    url = LOGIN_URL
    payload = {
        "email": "v@removespread.ru",
        "pass": "Qwerty123"
    }
    request = requests.post(url, json = payload)
    data = request.json()

    return data
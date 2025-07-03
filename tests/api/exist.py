import requests 

from tests.utils.generators import generate_valid_user_payload
from tests.variables.const import EXIST_URL

# Отправка запроса на ручку
# Отправляются данные существующего пользователя
def exist(email):
    url = EXIST_URL
    payload = {
        "email": email
    }
    request = requests.post(url, json = payload)

    return request

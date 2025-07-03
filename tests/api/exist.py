import requests 

from tests.utils.generators import generate_valid_user_payload
from tests.variables.const import EXIST_URL

# Отправка запроса на ручку
# Отправляются данные существующего пользователя
def exist():
    url = EXIST_URL
    payload = {
        "email": generate_valid_user_payload()["email"]
    }
    request = requests.post(url, json = payload)
    data = request.json()
    
    return data

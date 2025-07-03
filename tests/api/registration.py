import requests


from tests.utils.generators import generate_valid_user_payload # Импорт генератора
from tests.variables.const import LOGIN_URL, REGISTER_URL # Импорт всех API-URL

def register():
    url = REGISTER_URL
    payload = generate_valid_user_payload()
    request = requests.post(url, json = payload)
    
    data = request.json()
    
    return data

def login():
    url = LOGIN_URL
    payload = {
        "email": "v@removespread.ru",
        "pass": "Qwerty123"
    }
    request = requests.post(url, json = payload)
    data = request.json()

    return data
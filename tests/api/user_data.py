import requests 

from tests.api.login import login_exist_user
from tests.variables.const import USER_DATA

def rename_user():
    login_exist_user()
    
    return response.json()

def test_login_non_exist_user():
    url = USER_DATA
    payload = {
        "email": "imnotexistactually@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    return response.json()
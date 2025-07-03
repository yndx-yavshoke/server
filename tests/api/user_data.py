import requests 

from tests.api.login import login_exist_user
from tests.variables.const import USER_DATA

def get_actual_user():
    url = USER_DATA
    payload = {
        "email": "v@removespread.ru"
    }
    request = requests.post(url, json = payload)
    data = request.json()
    
    return data
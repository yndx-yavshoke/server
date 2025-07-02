import requests
import pytest
from .urls import Urls
from .endpoints import Endpoints
from .data import Login


@pytest.fixture
def get_token():
    data = Login.register
    response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', json=data)
    response_json = response.json() 
    return response_json.get('token')


#@pytest.fixture
#def auth_token():
 #   user_data = {...}  # ваши данные для входа
 #   response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', data=user_data)
  #  response_json = response.json()
  #  return response_json.get('token')
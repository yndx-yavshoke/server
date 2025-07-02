import allure
import pytest
import requests
from ..urls import Urls
from ..endpoints import Endpoints
from ..data import Login, NewName
from ..helps import NewNameCreate

@allure.title('Проверка смены имени авторизированного пользователя')
@allure.description('Отправляем запрос о переименовании с предварительной авторизацией')
def test_change_user_name_auth(get_token):
    obj = NewNameCreate()
    new_name = obj.get_name()
    headers = {
        'Authorization': f'Bearer {get_token}'
    }
    payload = {
        'name': new_name
    }
    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert 'name' in data['user']
    assert data['user']['name'] == new_name

@allure.title('Проверка смены имени без авторизации')
@allure.description('Отправляем запрос о переименовании без авторизации')
def test_change_user_name_not_auth():
    obj = NewNameCreate()
    new_name = obj.get_name()
    payload = {
        'name': new_name
    }
    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=payload)
    assert response.status_code == 401
    data = response.json()
    assert data['message'] == 'Authorization header required'

@allure.title('Проверка смены имени на пустое значение')
@allure.description('Отправляем запрос о переименовании на новое имя, поле оставляем пустым')
def test_change_user_name_validation_error(get_token):

    new_name = NewName.empty
    headers = {
        'Authorization': f'Bearer {get_token}'
    }
    payload = {
        'name': new_name
    }
    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=payload, headers=headers)
    assert response.status_code == 422
    data = response.json()
    assert data ['type'] == 'validation'



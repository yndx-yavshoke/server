import allure
import pytest
import requests
from ..urls import Urls
from ..endpoints import Endpoints
from ..data import Exist

@allure.title('Проверка шоковости')
@allure.description('''Отправляем запрос с указанием почты зарегистрированного пользователя''')
def test_exist_user():

    data = Exist.exist
    response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_exist}', json=data)
    assert response.status_code == 200

    responce = response.json()
    assert "exist" in responce
    assert responce["exist"] is True


@allure.title('Проверка шоковости')
@allure.description('''Отправляем запрос с указанием почты незарегистрированного пользователя''')
def test_not_exist_user():


    data = Exist.notexist
    response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_exist}', json=data)
    assert response.status_code == 200

    responce = response.json()
    assert "exist" in responce
    assert responce["exist"] is False
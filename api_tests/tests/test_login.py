import allure
import pytest
import requests
from ..urls import Urls
from ..endpoints import Endpoints
from ..data import Login

class TestUserLogin:
    @allure.title('Проверка пользователь может авторизоваться')
    @allure.description('Отправляем запрос с указанием почты зарегистрированного пользователя и верным паролем')
    def test_login_success(self):
        data = Login.register
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', json=data)
        assert response.status_code == 200

        response = response.json()
        assert 'token' in response

    @allure.title('Проверка авторизоваться под неверным паролем или несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('''Отправляем запрос с указанием почты зарегистрированного пользователя и неверным паролем или незарегистрированного пользователя и верным паролем''')
    @pytest.mark.parametrize('user_data', [Login.wrong_password,
                                           Login.not_register])
    def test_login_unsuccess(self, user_data):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', json=user_data)
        assert response.status_code == 422

        response = response.json()
        assert response.get('fields', {}).get('password') is not None
        assert 'Неправильный логин или пароль' in response['fields']['password']


    @allure.title('Проверка для авторизации нужно передать все обязательные поля Login/Password')
    @allure.description('''Отправляем запрос на авторизацию без заполнения обязательных полей Login/Password
                         и проверяем ответ''')
    @pytest.mark.parametrize('user_data', [Login.empty,
                                           Login.only_email, Login.only_password])
    def test_courier_login_without_parameters_failed(self, user_data):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', data=user_data)
        assert response.status_code == 422


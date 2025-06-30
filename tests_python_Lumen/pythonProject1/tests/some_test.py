import requests
import config
import pytest
from src.enums.global_enums import GlobalErrorMessages


# Перед тестами проверить файл config переменную SERVICE_URL
# для прода - "https://api.yavshok.ru/"
# Если подняли локально - "http://localhost:3000/" (проверить порт)
def test_check_conn():
    """
    Проверяем что вообще до сервера можем достучаться
    Это можно также перенести в conftest.py  в качестве фикстуры
    Но оставлю здесь для наглядности
    """

    url = config.SERVICE_URL + "exist/"
    try:
        response = requests.post(url=url, data={"email": "check_conn@check.conn"})
        if response.status_code != 200:
            pytest.exit("Не могу достучаться до сервера - дальше по тестам не иду")
    except requests.exceptions.RequestException:
        pytest.exit("Не могу подключиться к серверу - дальше по тестам не иду")

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE


def test_check_yavshoke_positive():
    """
    Проверяем что почта зарегистрированна
    """
    email = config.register_email_1
    data = {
        "email": email
    }
    url = config.SERVICE_URL + "exist/"
    response = requests.post(url=url, json=data)
    json_body = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert json_body.get("exist") is True, GlobalErrorMessages.WRONG_BODY


def test_check_yavshoke_negative():
    """
    Негативная проверка на шоковость
    """
    data = {"email": config.unregister_email}
    url = config.SERVICE_URL + "exist/"
    response = requests.post(url=url, json=data)
    json_body = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert json_body.get("exist") is False, GlobalErrorMessages.WRONG_BODY


# Можно подключить параметризацию чтобы сразу в одном методе проверить несколько пользователей
# @pytest.mark.parametrize("user_index", [0, 1, 2])
def test_check_auth_positive():
    """
    Пытаемся авторизоваться с уже зарегистирированными данными
    """
    email = config.register_email_1
    password = config.register_pass_1
    url = config.SERVICE_URL + "auth/login"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url=url, json=data)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE


def test_check_auth_negative():
    """
    Негативная проверка на авторизацию с незарегистрированной почтой
    """
    url = config.SERVICE_URL + "auth/login"
    data = {
        "email": config.unregister_email,
        "password": config.unregister_pass
    }
    response = requests.post(url=url, json=data)

    assert response.status_code == 422, GlobalErrorMessages.WRONG_STATUS_CODE


def test_swap_name():
    """
    Сначала логинемся, делаем запрос для получения действующего имени
    Меняем имя на имя из config переменная new_name
    Делаем новый запрос на получение действующего имени
    """

    email = config.register_email_1
    password = config.register_pass_1
    login_url = config.SERVICE_URL + "auth/login"
    auth_data = {
        "email": email,
        "password": password
    }
    login_response = requests.post(login_url, json=auth_data)
    assert login_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE

    token = login_response.json().get("token")
    assert token, GlobalErrorMessages.WRONG_TOKEN

    headers = {
        "Authorization": f"Bearer {token}"
    }
    user_info_url = config.SERVICE_URL + "user/me"
    response_before = requests.get(user_info_url, headers=headers)

    assert response_before.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE

    name_before = response_before.json().get("user", {}).get("name")
    print(f"Имя до: {name_before}")

    swap_name_url = config.SERVICE_URL + "user/name"
    switch_data = {
        "name": config.new_name
    }
    switch_response = requests.patch(swap_name_url, json=switch_data, headers=headers)
    assert switch_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE

    response_after = requests.get(user_info_url, headers=headers)
    assert response_after.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    name_after = response_after.json().get("user", {}).get("name")
    print(f"Имя после: {name_after}")

    assert name_after == config.new_name, (f" Имя не изменилось: ожидалось '{config.new_name}'"
                                           f", получено '{name_after}'")

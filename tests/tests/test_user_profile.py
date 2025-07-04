import requests
import pytest
from data import login_data


@pytest.mark.profile
def test_user_profile(base_url):
    url_me = f"{base_url}/user/me"
    url_login = f"{base_url}/auth/login"

    print(f"\nАвторизация пользователя с email: {login_data.registered_user['email']}...")
    response_login = requests.post(url_login, json=login_data.registered_user)
    data_login = response_login.json()
    status_code_login = response_login.status_code

    assert status_code_login == 200, f"\nСтатус-код: {status_code_login}, {data_login['fields']['password']}"
    print(f"Статус код: {status_code_login}, пользователь успешно вошел в систему!")
    
    print(f"\nПолучение данных о пользователе с email: {login_data.registered_user['email']}...")
    headers = {
        'Authorization': f"Bearer {data_login['token']}"
    }

    response_me = requests.get(url_me, headers=headers)
    data_me = response_me.json()
    status_code_me = response_me.status_code

    assert status_code_me == 200, f"Статус-код: {status_code_me}"
    print(f"Статус-код: {status_code_me}\nДанные о пользователе:\n{data_me}")




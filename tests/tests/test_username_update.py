import requests
import pytest
from data import update_username_data, login_data



@pytest.mark.update
def test_username_update_with_new_name_unregistered_user(base_url):
    url = f"{base_url}/user/name"
    url_login = f"{base_url}/auth/login"

    print(f"\nАвторизация зарегистрированного пользователя с email: {login_data.registered_user['email']}...")
    response_login = requests.post(url_login, json=login_data.registered_user)
    data_login = response_login.json()
    status_code_login = response_login.status_code

    assert status_code_login == 200, f"\nСтатус-код: {status_code_login}, {data_login['fields']['password']}"
    print(f"Статус код: {status_code_login}, пользователь успешно вошел в систему!")

    print(f"\nИзменение имени {data_login['user']['name']} пользователя с email: {login_data.registered_user['email']}...")
    headers = {
        'Authorization': f"Bearer {data_login['token']}"
    }

    response_update = requests.patch(url, json=update_username_data.new_username, headers=headers)
    data_update = response_update.json()
    status_code_update = response_update.status_code

    assert status_code_update == 200, f"\nСтатус-код: {status_code_update}"
    print(f"Статус код: {status_code_update}\nИмя пользователя {data_login['user']['name']} изменено на {data_update['user']['name']}")

@pytest.mark.update
def test_username_update_with_new_name_unregistered_user(base_url):
    url = f"{base_url}/user/name"
    url_login = f"{base_url}/auth/login"

    print(f"\nАвторизация незарегистрированного пользователя с email: {login_data.registered_user['email']}...")
    response_login = requests.post(url_login, json=login_data.unregistered_user)
    data_login = response_login.json()
    status_code_login = response_login.status_code

    assert status_code_login == 422, f"\nСтатус-код: {status_code_login}"
    print(f"Статус код: {status_code_login}\nСообщение: {data_login['fields']['password']}")

    print(f"\nИзменение имени незарегистрированного пользователя...")
    response_update = requests.patch(url, json=update_username_data.new_username)
    data_update = response_update.json()
    status_code_update = response_update.status_code

    assert status_code_update == 401, f"\nСтатус-код: {status_code_update}"
    print(f"Статус код: {status_code_update}\nСообщение: {data_update['message']}")

@pytest.mark.update
def test_username_update_with_new_name_invalid_password(base_url):
    url = f"{base_url}/user/name"
    url_login = f"{base_url}/auth/login"

    print(f"\nАвторизация пользователя с неверным паролем с email: {login_data.invalid_password['email']}...")
    response_login = requests.post(url_login, json=login_data.invalid_password)
    data_login = response_login.json()
    status_code_login = response_login.status_code

    assert status_code_login == 422, f"\nСтатус-код: {status_code_login}"
    print(f"Статус код: {status_code_login}\nСообщение: {data_login['fields']['password']}")

    print(f"\nИзменение имени незарегистрированного пользователя...")
    response_update = requests.patch(url, json=update_username_data.new_username)
    data_update = response_update.json()
    status_code_update = response_update.status_code

    assert status_code_update == 401, f"\nСтатус-код: {status_code_update}"
    print(f"Статус код: {status_code_update}\nСообщение: {data_update['message']}")
import requests
import pytest
from data import login_data


@pytest.mark.authorization
def test_user_authorization_with_registered_user(base_url):
    url = f"{base_url}/auth/login"
    response = requests.post(url, json=login_data.registered_user)
    data = response.json()
    status_code = response.status_code

    assert status_code == 200, f"\nСтатус-код: {status_code}, {data['fields']['password']}"
    print(f"\nСтатус код: {status_code}, пользователь с email {data['user']['email']} успешно вошел в систему!")

@pytest.mark.authorization
def test_user_authorization_with_unregistered_user(base_url):
    url = f"{base_url}/auth/login"
    response = requests.post(url, json=login_data.unregistered_user)
    data = response.json()
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}\nСообщение: {data['fields']['password']}")

@pytest.mark.authorization
def test_user_authorization_with_invalid_password(base_url):
    url = f"{base_url}/auth/login"
    response = requests.post(url, json=login_data.invalid_password)
    data = response.json()
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}\nСообщение: {data['fields']['password']}")

@pytest.mark.authorization
def test_user_authorization_with_empty_values(base_url):
    url = f"{base_url}/auth/login"
    response = requests.post(url, json=login_data.empty_values)
    data = response.json()
    status_code = response.status_code
    print(data)
    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"Статус код: {status_code}\nДанные не прошли валидацию")
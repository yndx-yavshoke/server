import requests
import pytest
from data import register_data


@pytest.mark.registration
def test_user_registration_with_unregistered_user(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.unregistered_user)
    data = response.json()
    status_code = response.status_code

    assert status_code == 200, f"\nСтатус-код: {status_code}\nСообщение: {data['fields']['email']}"
    print(f"\nСтатус код: {status_code}")

@pytest.mark.registration
def test_user_registration_with_registered_user(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.registered_user)
    data = response.json()
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}\nСообщение: {data['fields']['email']}")

@pytest.mark.registration
def test_user_registration_with_invalid_email(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.invalid_email)
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}")

@pytest.mark.registration
def test_user_registration_with_invalid_password(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.invalid_password)
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}")

@pytest.mark.registration
def test_user_registration_with_empty_values(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.empty_values)
    status_code = response.status_code

    assert status_code == 422, f"\nСтатус-код: {status_code}"
    print(f"\nСтатус код: {status_code}")

@pytest.mark.registration
def test_user_registration_with_min_age(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.min_age)
    data = response.json()
    status_code = response.status_code

    print(response.json())
    assert status_code == 200, f"\nСтатус-код: {status_code}\nСообщение: {data['fields']['email']}"
    print(f"\nСтатус код: {status_code}")

@pytest.mark.registration
def test_user_registration_with_max_age(base_url):
    url = f"{base_url}/auth/register"
    response = requests.post(url, json=register_data.max_age)
    data = response.json()
    status_code = response.status_code

    assert status_code == 200, f"\nСтатус-код: {status_code}\nСообщение: {data['fields']['email']}"
    print(f"\nСтатус код: {status_code}")
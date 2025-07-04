import pytest
import requests


from config import API_BASE_URL
from data.register import register_user_data


@pytest.fixture(scope="session")
def registered_user():
    requests.post(f"{API_BASE_URL}/auth/register", json=register_user_data)
    return register_user_data


@pytest.fixture(scope="module")
def authenticated_user_headers(registered_user):
    response = requests.post(f"{API_BASE_URL}/auth/login", json=registered_user)
    response.raise_for_status()
    token = response.json().get("token")

    if not token:
        raise Exception("Не удалось получить токен авторизации")

    headers = {
        "Authorization": f"Bearer {token}"
    }
    return headers


@pytest.fixture(scope="function")
def user(authenticated_user_headers):
    response = requests.get(
        f"{API_BASE_URL}/user/me",
        headers=authenticated_user_headers
    )
    return response.json()["user"]

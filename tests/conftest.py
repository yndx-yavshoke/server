import pytest
import requests

BASE_URL = "http://localhost:3000"

@pytest.fixture
def auth_token():
    """Фикстура для получения токена авторизации"""
    login_data = {
        "email": "testartem19@example.com",
        "password": "1234567"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    return response.json()["token"]
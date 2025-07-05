import pytest
import requests
import time


@pytest.fixture
def api_base_url():
    """Базовый URL для API"""
    return "http://localhost:3000"


@pytest.fixture
def unique_user_data():
    """Генерирует уникальные данные пользователя для каждого теста"""
    timestamp = int(time.time())
    return {
        "email": f"test_{timestamp}@example.com",
        "password": "123123123",
        "age": 22
    }


@pytest.fixture
def registered_user(api_base_url, unique_user_data):
    """Регистрирует пользователя и возвращает его данные"""
    register_url = f"{api_base_url}/auth/register"
    response = requests.post(register_url, json=unique_user_data)
    
    # Возвращаем данные пользователя (не важно зарегистрировался или уже существовал)
    return unique_user_data


@pytest.fixture 
def auth_token(api_base_url, registered_user):
    """Логинит пользователя и возвращает JWT токен"""
    login_url = f"{api_base_url}/auth/login"
    login_data = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }
    
    response = requests.post(login_url, json=login_data)
    assert response.status_code == 200
    
    return response.json()["token"]
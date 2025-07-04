import requests
import uuid
import pytest
from config import BASE_URL

# Позитивный тест на обновление имени пользователя
# Получаем токен
@pytest.fixture(scope="module")
def user_token():
    url_register = f"{BASE_URL}/auth/register"
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"
    payload = {
        "email": email,
        "password": password,
        "age": 25
    }
    requests.post(url_register, json=payload)
    url_login = f"{BASE_URL}/auth/login"
    login_payload = {
        "email": email,
        "password": password
    }
    login_response = requests.post(url_login, json=login_payload)
    return login_response.json()["token"]
# Обновляем имя пользователя
def test_update_user_name(user_token):
    url_update_name = f"{BASE_URL}/user/name"
    new_name = f"{uuid.uuid4().hex[:4]}"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": new_name}
    update_response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert update_response.status_code == 200
    # Проверяем, что имя обновлено
    data = update_response.json()
    assert "user" in data
    assert data["user"]["name"] == new_name

# Негативные тесты на обновление имени пользователя
def test_update_user_name_empty(user_token):
    url_update_name = f"{BASE_URL}/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": ""}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422, (
        f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
    )

def test_update_user_name_spaces(user_token):
    url_update_name = f"{BASE_URL}/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": "   "}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422, (
        f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
    )

def test_update_user_name_too_long(user_token):
    url_update_name = f"{BASE_URL}/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    long_name = "a" * 101  
    name_payload = {"name": long_name}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422, (
        f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
    )

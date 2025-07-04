import requests
import uuid
import random
from config import BASE_URL
from schemas import EXIST_USER_PAYLOAD, VALID_PASSWORD

# Позитивный тест на логин существующего пользователя
def test_login_existing_user_direct():
    url_login = f"{BASE_URL}/auth/login"
    login_payload = {
        "email": EXIST_USER_PAYLOAD["email"],
        "password": VALID_PASSWORD
    }
    response = requests.post(url_login, json=login_payload)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}, тело: {response.text}"
    )
    data = response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == EXIST_USER_PAYLOAD["email"]

# Негативные тесты на логин пользователя
def test_login_nonexistent_user():
    url_login = f"{BASE_URL}/auth/login"
    login_payload = {
        "email": f"random_{uuid.uuid4().hex[:8]}@example.com",  # несуществующий email
        "password": VALID_PASSWORD
    }
    login_response = requests.post(url_login, json=login_payload)
    assert login_response.status_code == 422, (
        f"Ожидался 422, получен {login_response.status_code}, тело: {login_response.text}"
    )

def test_login_wrong_password():
    url_login = f"{BASE_URL}/auth/login"
    login_payload = {
        "email": EXIST_USER_PAYLOAD["email"],
        "password": "wrongpassword"
    }
    response = requests.post(url_login, json=login_payload)
    assert response.status_code in (400, 401, 422), (
        f"Ожидался 400, 401 или 422, получен {response.status_code}, тело: {response.text}"
    )

def test_login_empty_email_and_password():
    url_login = f"{BASE_URL}/auth/login"
    login_payload = {
        "email": "",
        "password": ""
    }
    response = requests.post(url_login, json=login_payload)
    assert response.status_code in (400, 422), (
        f"Ожидался 400 или 422, получен {response.status_code}, тело: {response.text}"
    )

def test_login_invalid_email_format():
    url_login = f"{BASE_URL}/auth/login"
    special_chars = ''.join(random.choices('!@#$%^&*()[]{};:,.<>?/\\|`~', k=8))
    email = f"{special_chars}.ru"
    login_payload = {
        "email": email,
        "password": VALID_PASSWORD
    }
    response = requests.post(url_login, json=login_payload)
    assert response.status_code in (400, 422), (
        f"Ожидался 400 или 422, получен {response.status_code}, тело: {response.text}"
    )



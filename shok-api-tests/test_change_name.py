import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Конфиг
BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3000")
TEST_EMAIL = "e.sheluddd+8@gmail.com"
TEST_PASSWORD = "123123"

@pytest.fixture
def auth_token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": TEST_EMAIL, "password": TEST_PASSWORD}
    )
    
    if response.status_code != 200:
        pytest.fail(f"Ошибка авторизации: {response.status_code}\nResponse: {response.text}")
    
    return response.json().get("token")

def test_api_availability():
    response = requests.get(f"{BASE_URL}/health", timeout=3)
    assert response.status_code == 200, f"API недоступно. Status: {response.status_code}"

def test_unauthorized_name_change():
    response = requests.patch(
        f"{BASE_URL}/user/name",
        json={"name": "TestName"},
        timeout=3
    )
    assert response.status_code == 401

def test_successful_name_change(auth_token):
    # Успешное изменение имени пользователя
    test_name = "NewTestName123"
    
    response = requests.patch(
        f"{BASE_URL}/user/name",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={"name": test_name},
        timeout=3
    )
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert "user" in response_data
    assert response_data["user"]["name"] == test_name

@pytest.mark.parametrize("name,expected_status", [
    ("", 422),                # Пустое имя
    ("A", 200),               # Короткое имя (API принимает)
    ("X"*51, 422),            # Слишком длинное
    ("ValidName", 200),       # Валидное имя
    ("ИмяНаРусском", 200),    # Русские буквы
    ("name-with-hyphen", 200) # Дефисы
])
def test_name_variations(auth_token, name, expected_status):
    response = requests.patch(
        f"{BASE_URL}/user/name",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={"name": name},
        timeout=3
    )
   
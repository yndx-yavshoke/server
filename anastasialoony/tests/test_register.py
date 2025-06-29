
import requests
import uuid
import random

def test_register_new_user():
    url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    unique_age = random.randint(0, 99)
    payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": unique_age
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200 or response.status_code == 201

    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == payload["email"]
    assert data["user"]["age"] == payload["age"]

def test_register_existing_user():
    url = "http://localhost:3000/auth/register"
    payload = {
        "email": "newuser123@example.com", 
        "password": "TestPassword123",
        "age": 25
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "email" in data["fields"]


def test_register_with_invalid_email():
    url = "http://localhost:3000/auth/register"
    payload = {
        "email": "null",
        "password": "TestPassword123",
        "age": 25
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 422 or response.status_code == 400

def test_register_with_invalid_age():
    url = "http://localhost:3000/auth/register"
    unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    invalid_age = random.randint(-100, -1)
    payload = {
        "email": unique_email,
        "password": "TestPassword123",
        "age": invalid_age 
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 422 or response.status_code == 400

def test_register_with_too_long_email():
    url = "http://localhost:3000/auth/register"
    # Генерируем email длиной 51 символ (например, 40 символов имя + 11 символов домен)
    unique_part = uuid.uuid4().hex[:10]
    local_part = "a" * 35 + unique_part  # 35 + 10 = 45 символов
    domain = "b" * 7  # 7 символов
    too_long_email = f"{local_part}@{domain}.com"  # 45 + 1 + 7 + 4 = 57 символов
    
    payload = {
        "email": too_long_email,
        "password": "TestPassword123",
        "age": 25
    }
    response = requests.post(url, json=payload)
    # Ожидаем ошибку 422 или 400
    assert response.status_code == 422 or response.status_code == 400
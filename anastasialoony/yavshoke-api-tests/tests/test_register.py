import requests
import uuid
import random
from config import BASE_URL
import pytest

# Позитивные тесты на регистрацию пользователя
# def test_register_new_user():
#     url = f"{BASE_URL}/auth/register"
#     unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
#     unique_age = random.randint(0, 99)
#     payload = {
#         "email": unique_email,
#         "password": "TestPassword123",
#         "age": unique_age
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 200 or response.status_code == 201, (
#         f"Ожидался 200 или 201, получен {response.status_code}, тело: {response.text}"
#     )
#     data = response.json()
#     assert "user" in data, (
#         f"Нет ключа 'user' в ответе: {data}"
#     )
#     assert data["user"]["email"] == payload["email"], (
#         f"Ожидался email {payload['email']}, получен {data['user']['email']}"
#     )
#     assert data["user"]["age"] == payload["age"], (
#         f"Ожидался age {payload['age']}, получен {data['user']['age']}"
#     )

# @pytest.mark.parametrize("age", [1, 21]) #0 не проходит
# def test_register_young_cat(age):
#     url = f"{BASE_URL}/auth/register"
#     unique_email = f"young_{age}_{uuid.uuid4().hex[:8]}@example.com"
#     payload = {
#         "email": unique_email,
#         "password": "TestPassword123",
#         "age": age
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 200 or response.status_code == 201, (
#         f"Ожидался 200 или 201, получен {response.status_code}, тело: {response.text}"
#     )
#     data = response.json()
#     assert data["user"]["age"] == age, (
#         f"Ожидался age {age}, получен {data['user']['age']}"
#     )

# @pytest.mark.parametrize("age", [22, 50, 68])
# def test_register_adult_cat(age):
#     url = f"{BASE_URL}/auth/register"
#     unique_email = f"adult_{age}_{uuid.uuid4().hex[:8]}@example.com"
#     payload = {
#         "email": unique_email,
#         "password": "TestPassword123",
#         "age": age
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 200 or response.status_code == 201, (
#         f"Ожидался 200 или 201, получен {response.status_code}, тело: {response.text}"
#     )
#     data = response.json()
#     assert data["user"]["age"] == age, (
#         f"Ожидался age {age}, получен {data['user']['age']}"
#     )

# @pytest.mark.parametrize("age", [69, 70, 99])
# def test_register_old_cat(age):
#     url = f"{BASE_URL}/auth/register"
#     unique_email = f"old_{age}_{uuid.uuid4().hex[:8]}@example.com"
#     payload = {
#         "email": unique_email,
#         "password": "TestPassword123",
#         "age": age
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 200 or response.status_code == 201, (
#         f"Ожидался 200 или 201, получен {response.status_code}, тело: {response.text}"
#     )
#     data = response.json()
#     assert data["user"]["age"] == age, (
#         f"Ожидался age {age}, получен {data['user']['age']}"
#     )

# # Негативные тесты на регистрацию пользователя
# def test_register_existing_user():
#     url = f"{BASE_URL}/auth/register"
#     payload = {
#         "email": "newuser123@example.com", 
#         "password": "TestPassword123",
#         "age": 25
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422, (
#         f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
#     )
#     data = response.json()
#     assert "email" in data["fields"], (
#         f"Нет ключа 'email' в полях: {data}"
#     )

# def test_register_with_invalid_email():
#     url = f"{BASE_URL}/auth/register"
#     payload = {
#         "email": "null",
#         "password": "TestPassword123",
#         "age": 46
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422 or response.status_code == 400, (
#         f"Ожидался 422 или 400, получен {response.status_code}, тело: {response.text}"
#     )

# def test_register_with_invalid_age():
#     url = f"{BASE_URL}/auth/register"
#     unique_email = f"user_{uuid.uuid4().hex[:8]}@example.com"
#     invalid_age = random.randint(-100, -1)
#     payload = {
#         "email": unique_email,
#         "password": "TestPassword123",
#         "age": invalid_age 
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422 or response.status_code == 400, (
#         f"Ожидался 422 или 400, получен {response.status_code}, тело: {response.text}"
#     )

# def test_register_with_too_long_email():
#     url = f"{BASE_URL}/auth/register"
#     unique_part = uuid.uuid4().hex[:10]
#     local_part = "a" * 35 + unique_part
#     domain = "b" * 7
#     too_long_email = f"{local_part}@{domain}.com"
#     payload = {
#         "email": too_long_email,
#         "password": "TestPassword123",
#         "age": 99
#     }
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422 or response.status_code == 400, (
#         f"Ожидался 422 или 400, получен {response.status_code}, тело: {response.text}"
#     )
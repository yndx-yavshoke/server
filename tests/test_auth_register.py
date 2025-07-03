import requests
import uuid

BASE_URL = "http://localhost:3000/auth/register"


def test_user_register():
    random_part = uuid.uuid4().hex[:4]
    email = f"test{random_part}@example.com"

    payload = {
        "email": email,
        "password": "test2906",
        "age": 38
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert "user" in data


def test_exist_user_register():
    payload = {
        "email": "test123user@test.com",
        "password": "test2906",
        "age": 38
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 422


def test_wrong_password():
    payload = {
        "email": "test123user@test.com",
        "password":  uuid.uuid4().hex[:6],
        "age": 38
    }

    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 422

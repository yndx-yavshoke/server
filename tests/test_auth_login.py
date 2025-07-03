import requests
import uuid

BASE_URL = "http://localhost:3000/auth/login"

def test_user_login():
    random_part = uuid.uuid4().hex[:4]
    email = f"test{random_part}@example.com"
    password = "Test2906"
    payload_register = {
        "email": email,
        "password": password,
        "age": 38
    }
    register_url = "http://localhost:3000/auth/register"
    register_response = requests.post(register_url, json=payload_register)
    assert register_response.status_code == 200

    payload_login = {
        "email": email,
        "password": password
    }
    login_response = requests.post(BASE_URL, json=payload_login)
    assert login_response.status_code == 200
    data = login_response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == email

def test_user_login_nonexistent():
    email = f"test{uuid.uuid4().hex[:4]}@example.com"
    password = "WrongPassword123"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 422
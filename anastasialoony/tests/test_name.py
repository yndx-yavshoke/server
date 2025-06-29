import requests
import uuid
import pytest

@pytest.fixture(scope="module")
def user_token():
    url_register = "http://localhost:3000/auth/register"
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"
    payload = {
        "email": email,
        "password": password,
        "age": 25
    }
    requests.post(url_register, json=payload)
    url_login = "http://localhost:3000/auth/login"
    login_payload = {
        "email": email,
        "password": password
    }
    login_response = requests.post(url_login, json=login_payload)
    return login_response.json()["token"]

def test_update_user_name(user_token):
    url_update_name = "http://localhost:3000/user/name"
    new_name = f"{uuid.uuid4().hex[:4]}"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": new_name}
    update_response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert update_response.status_code == 200
    
    data = update_response.json()
    assert "user" in data
    assert data["user"]["name"] == new_name

def test_update_user_name_empty(user_token):
    url_update_name = "http://localhost:3000/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": ""}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422

def test_update_user_name_spaces(user_token):
    url_update_name = "http://localhost:3000/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    name_payload = {"name": "   "}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422

def test_update_user_name_too_long(user_token):
    url_update_name = "http://localhost:3000/user/name"
    headers = {"Authorization": f"Bearer {user_token}"}
    long_name = "a" * 101  
    name_payload = {"name": long_name}
    response = requests.patch(url_update_name, json=name_payload, headers=headers)
    assert response.status_code == 422

# Tests for POST /auth/login, for sign in

import requests

BASE_URL = "http://localhost:3000"
# from utils.constants import BASE_URL

def test_user_login_success():
    data = {
        "email": "molodoy@gmail.com",
        "password": "12345678"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=data)

    assert response.status_code == 200
    assert "token" in response.json()
    assert "user" in response.json()

def test_user_login_failure():
    data = {
        "email": "__#ir3r9u2ru20ru3ru2ofh23ugf2iougb442429g4gmolodoy@gmail.com",
        "password": "1234556789"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    assert response.status_code == 422
    assert "fields" in response.json()
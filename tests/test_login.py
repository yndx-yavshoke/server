import requests

from config import API_BASE_URL
from data.register import unregistered_user_data


def test_login_registered_user(registered_user):
    response = requests.post(f"{API_BASE_URL}/auth/login", json=registered_user)
    assert response.status_code == 200
    assert "token" in response.json()


def test_login_wrong_password(registered_user):
    wrong_password_data = {
        "email": registered_user["email"],
        "password": "wrong_password"
    }
    response = requests.post(f"{API_BASE_URL}/auth/login", json=wrong_password_data)
    assert response.status_code == 422


def test_email_wrong_password(registered_user):
    wrong_email_data = {
        "email": "wrong_password",
        "password": registered_user["password"]
    }
    response = requests.post(f"{API_BASE_URL}/auth/login", json=wrong_email_data)
    assert response.status_code == 422


def test_login_unregistered_user():
    response = requests.post(f"{API_BASE_URL}/auth/login", json=unregistered_user_data)
    assert response.status_code == 422

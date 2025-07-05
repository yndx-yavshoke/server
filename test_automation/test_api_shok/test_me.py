# GET /user/me

import requests

BASE_URL = "http://localhost:3000"
# from utils.constants import BASE_URL

def test_get_user_me_success(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/user/me", headers=headers)

    assert response.status_code == 200
    user = response.json()["user"]

    assert isinstance(user["id"], int)
    assert "email" in user
    assert "name" in user
    assert isinstance(user["age"], int)

def test_get_user_me_unauthorized():
    response = requests.get(f"{BASE_URL}/user/me")
    assert response.status_code == 401
    assert "message" in response.json()

def test_get_user_me_with_invalid_token():
    headers = {"Authorization": "Bearer faketoken123"}
    response = requests.get(f"{BASE_URL}/user/me", headers=headers)

    assert response.status_code == 401
    assert "message" in response.json()

def test_user_me_age_range(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(f"{BASE_URL}/user/me", headers=headers)
    age = response.json()["user"]["age"]

    assert 0 <= age <= 99

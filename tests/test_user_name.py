import requests
import uuid
import random
import string

BASE_URL = "http://localhost:3000/user/name"


def test_change_name():
    # make new user
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
    token = register_response.json()["token"]

    new_name = ''.join(random.choices(string.ascii_letters, k=6))
    payload_change_name = {
        "name": new_name
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    change_name_response = requests.patch(BASE_URL, json=payload_change_name, headers=headers)
    assert change_name_response.status_code == 200
    data = change_name_response.json()
    assert "user" in data
    assert data["user"]["name"] == new_name


def test_change_name_without_token():
    new_name = ''.join(random.choices(string.ascii_letters, k=6))
    payload_change_name = {
        "name": new_name
    }

    response = requests.patch(BASE_URL, json=payload_change_name)

    assert response.status_code == 401
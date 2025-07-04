import requests
import random
import string
import uuid

RENAME_URL = "http://localhost:3000/user/name"
REGISTER_URL = "http://localhost:3000/auth/register"

# Valid rename test, 10 keys for name
def test_valid_rename():
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = "Qwerty123"

    # Register payload == body for request
    payload = {
        "email": email,
        "password": password,
        "age": 38
    }
    response = requests.post(REGISTER_URL, json=payload)
    assert response.status_code == 200
    token = response.json()["token"]

    # 10 keys for name
    rename_variable = ''.join(random.choices(string.ascii_letters, k=10))

    # Rename payload == body for request
    payload = {
        "name": rename_variable
    }

    # Headers payload for patch request
    headers = {
        "Authorization": f"Bearer {token}"
    }

    change_name_response = requests.patch(RENAME_URL, json=payload, headers=headers)
    assert change_name_response.status_code == 200

    data = change_name_response.json()
    assert "user" in data
    assert data["user"]["name"] == rename_variable

def test_unvalid_rename():
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = "Qwerty123"

    # Register payload == body for request
    payload = {
        "email": email,
        "password": password,
        "age": 38
    }
    response = requests.post(REGISTER_URL, json=payload)
    assert response.status_code == 200
    token = response.json()["token"]

    # 70 keys for name
    rename_variable = ''.join(random.choices(string.ascii_letters, k=70))

    # Rename payload == body for request
    payload = {
        "name": rename_variable
    }

    # Headers payload for patch request
    headers = {
        "Authorization": f"Bearer {token}"
    }

    change_name_response = requests.patch(RENAME_URL, json=payload, headers=headers)
    assert change_name_response.status_code == 422

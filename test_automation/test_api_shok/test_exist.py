# Tests for method POST/exist, check if user exists

import requests
import random

BASE_URL = "http://localhost:3000"
# from utils.constants import BASE_URL

def test_user_exists():
    payload = {"email": "serzh52@list.ru"}
    response = requests.post(f"{BASE_URL}/exist", json=payload)
    assert response.json()["exist"] is True


def test_user_does_not_exist():
    email = f"definitelynotexistednewuser{random.randint(10000, 99999)}@example.com"
    payload = {"email": email}
    response = requests.post(f"{BASE_URL}/exist", json=payload)

    assert response.status_code == 200
    assert response.json()["exist"] is False
import pytest
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_URL = "http://localhost:3000"
# from utils.constants import BASE_URL

@pytest.fixture
def auth_token():
    creds = {
        "email": "101010@mail.com",
        "password": "123456"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=creds)
    return response.json()["token"]

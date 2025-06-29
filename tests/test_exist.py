import pytest
import requests

def test_exist_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "test@removespread.ru"
    }

    response = requests.post(url, json = payload)
    assert response.status_code == 200
    data = response.json
    assert data["exist"] is True

def test_exist_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "imnotexist@removespread.ru"
    }

    response = requests.post(url, json = payload)
    assert response.status_code == 200
    data = response.json
    assert data["exist"] is False

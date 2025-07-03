import pytest
import requests


def test_user_exist():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "hi@mail.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "exist" in data
    assert data["exist"] is True


def test_user_not_exist():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "bye@mail.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is False

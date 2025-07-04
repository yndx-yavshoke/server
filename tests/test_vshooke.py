import requests

from config import API_BASE_URL
from data.register import unregistered_user_data


def test_vshooke_registered_user(registered_user):
    data = {
        "email": registered_user["email"]
    }
    response = requests.post(f"{API_BASE_URL}/exist", json=data)
    assert response.status_code == 200
    assert response.json()["exist"] == True


def test_vshooke_unregistered_user():
    data = {
        "email": unregistered_user_data["email"]
    }
    response = requests.post(f"{API_BASE_URL}/exist", json=data)
    assert response.status_code == 200
    assert response.json()["exist"] == False



def test_vshooke_empty_data():
    data = {}
    response = requests.post(f"{API_BASE_URL}/exist", json=data)
    assert response.status_code == 422
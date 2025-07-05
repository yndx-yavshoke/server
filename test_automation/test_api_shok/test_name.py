import requests

BASE_URL = "http://localhost:3000"
#from utils.constants import BASE_URL

def test_change_username(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    payload = {"name": "YetAnotherJuniorYandexQA"}
    response = requests.patch(f"{BASE_URL}/user/name", headers=headers, json=payload)

    assert response.status_code == 200
    assert response.json()["user"]["name"] == "YetAnotherJuniorYandexQA"

def test_change_name_without_token():
    payload = {"name": "No Token User"}
    response = requests.patch(f"{BASE_URL}/user/name", json=payload)

    assert response.status_code == 401
    assert "message" in response.json()

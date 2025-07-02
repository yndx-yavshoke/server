import requests
from functions import url


def test_exist_user():
    url_check = url+ "/exist"
    payload = {
        "email": "user@example.com"
    }
    response = requests.post(url_check, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is True


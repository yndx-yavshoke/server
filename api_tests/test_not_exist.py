import requests
from functions import generate_valid_email,url

def test_not_exist_user():
    url_check = url+ "/exist"

    random_email = generate_valid_email()
    payload = {
        "email": f"{random_email}@example.com"
    }
    response = requests.post(url_check, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is False
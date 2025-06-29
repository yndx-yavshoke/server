import requests

def test_exist_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "test@yandex.ru"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is True


def test_not_exist_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "no_such_user@example.com"  
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is False 
import requests

def test_existed_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "v@removespread.ru"
    }
    request = requests.post(url, json = payload)
    assert request.status_code == 200

    data = request.json()

    assert data["exist"] is True

def test_nonexisted_user():
    url = "http://localhost:3000/exist"
    payload = {
        "email": "nonexisted@removespread.ru"
    }
    request = requests.post(url, json = payload)
    assert request.status_code == 200

    data = request.json()

    assert data["exist"] is False
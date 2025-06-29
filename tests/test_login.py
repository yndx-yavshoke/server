import requests 

def test_login_exist_user():
    url = "http://localhost:3000/login"
    payload = {
        "email": "test@removespread.ru",
        "password": "Qwerty123"
    }

    response = requests.post(url, json = payload)
    assert response.status_code == 200
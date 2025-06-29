import requests
import uuid

def test_get_user_me_success():
    # Получаем токен
    url_register = "http://localhost:3000/auth/register"
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"
    payload = {
        "email": email,
        "password": password,
        "age": 25
    }
    requests.post(url_register, json=payload)
    url_login = "http://localhost:3000/auth/login"
    login_payload = {
        "email": email,
        "password": password
    }
    login_response = requests.post(url_login, json=login_payload)
    token = login_response.json()["token"]

    # GET /user/me с токеном
    url_me = "http://localhost:3000/user/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url_me, headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == email

def test_get_user_me_unauthorized():
    url_me = "http://localhost:3000/user/me"
    response = requests.get(url_me)  # без Authorization
    assert response.status_code == 401 
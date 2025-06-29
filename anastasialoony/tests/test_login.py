import requests
import uuid

def test_login_existing_user():
    # Сначала регистрируем пользователя
    url_register = "http://localhost:3000/auth/register"
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123"
    payload = {
        "email": email,
        "password": password,
        "age": 25
    }
    response = requests.post(url_register, json=payload)
    assert response.status_code in [200, 201]

    # Теперь логинимся этим пользователем
    url_login = "http://localhost:3000/auth/login"
    login_payload = {
        "email": email,
        "password": password
    }
    login_response = requests.post(url_login, json=login_payload)
    assert login_response.status_code == 200
    data = login_response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == email

def test_login_nonexistent_user():
    url_login = "http://localhost:3000/auth/login"
    login_payload = {
        "email": f"random_{uuid.uuid4().hex[:8]}@example.com",  # точно несуществующий email
        "password": "WrongPassword123"
    }
    login_response = requests.post(url_login, json=login_payload)
    assert login_response.status_code == 422
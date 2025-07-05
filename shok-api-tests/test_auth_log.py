import pytest
import requests
BASE_URL = "http://localhost:3000"
class AuthAPIClient:
    def __init__(self):
        self.base_url = f"{BASE_URL}/auth"
    
    def login(self, email: str, password: str):
        response = requests.post(
            f"{self.base_url}/login",
            json={"email": email, "password": password}
        )
        return response

@pytest.fixture
def api_client():
    return AuthAPIClient()

# 1. Тест с существующими данными
def test_valid_credentials(api_client):

    response = api_client.login(
        email="e.sheluddd+8@gmail.com",  
        password="123123"               
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert data["user"]["email"] == "e.sheluddd+8@gmail.com"

# 2. Тест с несуществующими данными
def test_nonexistent_credentials(api_client):
    response = api_client.login(
        email="notexist123@example.com", 
        password="randompassword123"
    )
    
    assert response.status_code == 422  # Ожидаем ошибку валидации

# 3. Тест с некорректным email
def test_invalid_email_format(api_client):
    response = api_client.login(
        email="1234567890",
        password="password123"
    )
    
    assert response.status_code == 422  # Ожидаем ошибку валидации

# 4. Тест на вход без пароля
def test_short_password(api_client):
    response = api_client.login(
        email="valid@example.com",      
        password=""                
    )
    
    assert response.status_code == 422  # Ожидаем ошибку валидации


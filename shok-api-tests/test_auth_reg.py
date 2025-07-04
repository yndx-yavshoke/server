import requests
import uuid
import random

BASE_URL = "http://localhost:3000"

def test_registration_user():
    #регистрация нового пользователя
    test_user = {
        "email": f"test_{uuid.uuid4().hex[:6]}@test.com",
        "password": "Pass123",
        "age": random.randint(18, 99)
    }
    
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=test_user
    )
    
    assert response.status_code in (200, 201)
    
    user_data = response.json().get("user", {})
    assert user_data
    assert user_data["email"] == test_user["email"]
    assert user_data["age"] == test_user["age"]
    assert user_data.get("name") == "Neko"


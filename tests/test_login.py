import pytest
import requests

BASE_URL = "http://localhost:3000" 

TEST_CASES = [
    ("testartem19@example.com", "1234567", 200),
    ("testartem40@example.com", "1234567", 200),
    ("testartem@example.com", "1234567", 200),
    ("testnotartem19@example.com", "1234567", 422),
    ("testartem19@example.com", "1234567890", 422),
]

@pytest.mark.parametrize("email, password, expected_status", TEST_CASES)
def test_user_login_young(email, password, expected_status):
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password}
    )

    assert response.status_code == expected_status, (
        f"Ожидался статус {expected_status}, получен {response.status_code}"
    )

    if expected_status == 200:
        response_data = response.json()
        assert "token" in response_data, "Нет поля 'token' в ответе"
        assert "user" in response_data, "Нет поля 'user' в ответе"
        user_data = response_data["user"]
        assert "id" in user_data, "Нет поля 'id' в user"
        assert "email" in user_data, "Нет поля 'email' в user"
        assert "name" in user_data, "Нет поля 'name' в user"
        assert "age" in user_data, "Нет поля 'age' в user"


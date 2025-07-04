import requests

BASE_URL = "http://localhost:3000"

def test_existing_user():
    # Проверяем существующего пользователя
    response = requests.post(
        f"{BASE_URL}/exist",
        json={"email": "e.sheluddd+8@gmail.com"}
    )

    assert response.status_code == 200
    result = response.json()

    assert "exist" in result
    assert isinstance(result["exist"], bool)
    assert result["exist"] is True

def test_nonexistent_user():
    # Проверяем несуществующего пользователя
    response = requests.post(
        f"{BASE_URL}/exist",
        json={"email": f"nonexistent_{requests.utils.quote('тест@example.com')}"}
    )

    assert response.status_code == 200
    result = response.json()

    assert "exist" in result
    assert isinstance(result["exist"], bool)
    assert result["exist"] is False


import pytest
import requests

BASE_URL = "http://localhost:3000" 


TEST_CASES = [
    # (name, auth, expected_status, description)
    ("NewName", True, 200, "Успешное обновление имени"),
    ("", True, 422, "Пустое имя"),
    ("X" * 101, True, 422, "Слишком длинное имя"),
    ("ValidName", False, 401, "Отсутствие токена"),
]

@pytest.mark.parametrize("name, auth, expected_status, description", TEST_CASES)
def test_user_change_name(auth_token, name, auth, expected_status, description):
    headers = {
        "Content-Type": "application/json",
    }

    if auth:
        headers["Authorization"] = f"Bearer {auth_token}"

    response = requests.patch(
        f"{BASE_URL}/user/name",
        json={"name": name},
        headers=headers
    )

    assert response.status_code == expected_status, (
        f"{description} Ожидался {expected_status}, получен {response.status_code}"
    )

    if expected_status == 200:
        response_data = response.json()
        assert "user" in response_data
        assert response_data["user"]["name"] == name
    elif expected_status == 401:
        assert "message" in response.json()
    elif expected_status == 422:
        assert "found" in response.json()
        assert "type" in response.json()


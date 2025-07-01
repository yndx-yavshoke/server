import pytest
import requests

BASE_URL = "http://localhost:3000" 


def test_check_user_exist():
    test_data = {
        "email": "testartem@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/exist",
        json=test_data
    )

    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )

    response_data = response.json()

    assert "exist" in response_data
    assert response_data["exist"] is True

def test_check_user_not_exist():
    test_data = {
        "email": "testnotartem@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/exist",
        json=test_data
    )

    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )

    response_data = response.json()

    assert "exist" in response_data
    assert response_data["exist"] is False
    
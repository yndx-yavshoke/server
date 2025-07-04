import requests
import uuid
from config import BASE_URL
from schemas import VALID_PASSWORD, VALID_TOKEN, EXIST_USER_PAYLOAD

# Позитивный тест на получение информации о пользователе
def test_get_user_me_success():
    # GET /user/me с токеном
    url_me = f"{BASE_URL}/user/me"
    headers = {"Authorization": f"Bearer {VALID_TOKEN}"}
    response = requests.get(url_me, headers=headers)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}, тело: {response.text}"
    )
    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == EXIST_USER_PAYLOAD["email"]

# Негативный тест на получение информации о пользователе
def test_get_user_me_unauthorized():
    url_me = f"{BASE_URL}/user/me"
    response = requests.get(url_me)  # без Authorization
    assert response.status_code == 401, (
        f"Ожидался 401, получен {response.status_code}, тело: {response.text}"
    ) 
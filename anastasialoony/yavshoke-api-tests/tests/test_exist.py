import requests
from config import BASE_URL
from schemas import EXIST_USER_PAYLOAD, NOT_EXIST_USER_PAYLOAD

# Позитивные тесты на проверку существующего и несуществующего пользователя
def test_exist_user():
    url = f"{BASE_URL}/exist"
    payload = EXIST_USER_PAYLOAD
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}, тело: {response.text}"
    )
    data = response.json()
    assert "exist" in data
    assert data["exist"] is True

def test_not_exist_user():
    url = f"{BASE_URL}/exist"
    payload = NOT_EXIST_USER_PAYLOAD
    response = requests.post(url, json=payload)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}, тело: {response.text}"
    )
    data = response.json()
    assert "exist" in data
    assert data["exist"] is False 

# Негативные тесты на проверку поля ввода email (фейлятся)

# def test_exist_user_no_domain():
#     url = f"{BASE_URL}/exist"
#     payload = {"email": "test@"}
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422, (
#         f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
#     )

# def test_exist_user_no_at_symbol():
#     url = f"{BASE_URL}/exist"
#     payload = {"email": "testyandex.ru"}
#     response = requests.post(url, json=payload)
#     assert response.status_code == 422, (
#         f"Ожидался 422, получен {response.status_code}, тело: {response.text}"
#     )


    
import pytest
from endpoints.auth_endpoint import AuthEndpoint
from utils.data_generator import generate_valid_user_payload
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Тест на успешное получение данных текущего пользователя
# Сначала регистрируем пользователя, затем получаем токен и делаем запрос /user/me

def test_get_user_me_success(api_client, base_url):
    user_payload = generate_valid_user_payload()
    auth_endpoint = AuthEndpoint(api_client, base_url)
    reg_response = auth_endpoint.register(user_payload)
    token = reg_response.json()["token"]

    api_client.headers["Authorization"] = f"Bearer {token}"

    response = api_client.get(f"{base_url}/user/me")
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == user_payload["email"]
    assert data["user"]["age"] == user_payload["age"]

# Тест на получение данных пользователя без токена (должен вернуть 401)

def test_get_user_me_unauthorized(api_client, base_url):
    # Убираем токен
    api_client.headers.pop("Authorization", None)
    response = api_client.get(f"{base_url}/user/me")
    assert response.status_code == 401
    data = response.json()
    assert "message" in data

from utils.data_generator import generate_valid_user_payload, generate_name_update_payload

# Тест на успешное обновление имени пользователя
# Сначала регистрируем и логиним пользователя, затем обновляем имя

def test_update_user_name_success(api_client, base_url):
    user_payload = generate_valid_user_payload()
    auth_endpoint = AuthEndpoint(api_client, base_url)
    auth_endpoint.register(user_payload)
    login_response = auth_endpoint.login({
        "email": user_payload["email"],
        "password": user_payload["password"]
    })
    token = login_response.json()["token"]
    api_client.headers["Authorization"] = f"Bearer {token}"

    # Обновляем имя
    new_name = "TestName"
    response = api_client.patch(f"{base_url}/user/name", json={"name": new_name})
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["name"] == new_name

# Тест на обновление имени без авторизации (должен вернуть 401)

def test_update_user_name_unauthorized(api_client, base_url):
    api_client.headers.pop("Authorization", None)
    response = api_client.patch(f"{base_url}/user/name", json={"name": "TestName"})
    assert response.status_code == 401
    data = response.json()
    assert "message" in data

# Тест на обновление имени на невалидное значение (например, пустая строка)
# Ожидается ошибка 422

def test_update_user_name_invalid(api_client, base_url):
    user_payload = generate_valid_user_payload()
    auth_endpoint = AuthEndpoint(api_client, base_url)
    auth_endpoint.register(user_payload)
    login_response = auth_endpoint.login({
        "email": user_payload["email"],
        "password": user_payload["password"]
    })
    token = login_response.json()["token"]
    api_client.headers["Authorization"] = f"Bearer {token}"

    # Пытаемся обновить имя на невалидное (например, пустая строка)
    response = api_client.patch(f"{base_url}/user/name", json={"name": ""})
    assert response.status_code == 422

# Smoke-тест на получение данных текущего пользователя (/user/me)
@pytest.mark.smoke
def test_smoke_user_me(api_client, base_url):
    user_payload = generate_valid_user_payload()
    auth_endpoint = AuthEndpoint(api_client, base_url)
    reg_response = auth_endpoint.register(user_payload)
    token = reg_response.json()["token"]
    api_client.headers["Authorization"] = f"Bearer {token}"
    response = api_client.get(f"{base_url}/user/me")
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert data["user"]["email"] == user_payload["email"]
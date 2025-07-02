import pytest
from endpoints.exist_endpoint import ExistEndpoint
from endpoints.auth_endpoint import AuthEndpoint
from utils.data_generator import generate_valid_user_payload

# Тест на существование пользователя: сначала регистрируем, потом проверяем exist

def test_exist_user_true(api_client, base_url):
    # Сначала регистрируем пользователя
    user_payload = generate_valid_user_payload()
    AuthEndpoint(api_client, base_url).register(user_payload)
    # Проверяем, что exist возвращает true
    endpoint = ExistEndpoint(api_client, base_url)
    response = endpoint.check_exist({"email": user_payload["email"]})
    assert response.status_code == 200
    data = response.json()
    assert data["exist"] is True

# Тест на несуществующего пользователя: используем email, который точно не зарегистрирован

def test_exist_user_false(api_client, base_url):
    # Используем email, который точно не зарегистрирован
    fake_email = "not_exist_{}@example.com".format(id(object()))
    endpoint = ExistEndpoint(api_client, base_url)
    response = endpoint.check_exist({"email": fake_email})
    assert response.status_code == 200
    data = response.json()
    assert data["exist"] is False

# Тест на невалидный email (формат), но сервер всё равно возвращает 200

def test_exist_invalid_email(api_client, base_url):
    endpoint = ExistEndpoint(api_client, base_url)
    response = endpoint.check_exist({"email": "not-an-email"})
    assert response.status_code == 200

# Smoke-тест на проверку существования пользователя (/exist)
@pytest.mark.smoke
def test_smoke_exist(api_client, base_url):
    user_payload = generate_valid_user_payload()
    AuthEndpoint(api_client, base_url).register(user_payload)
    endpoint = ExistEndpoint(api_client, base_url)
    response = endpoint.check_exist({"email": user_payload["email"]})
    assert response.status_code == 200
    data = response.json()
    assert "exist" in data
    assert data["exist"] is True
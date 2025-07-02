from endpoints.auth_endpoint import AuthEndpoint
from utils.data_generator import generate_valid_user_payload, generate_invalid_user_payload
import pytest

# Тест на успешную регистрацию пользователя с валидными данными
# Ожидается, что имя будет присвоено 'Neko', а email и age совпадут с отправленными

def test_registration_with_valid_data(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()  # генерируем валидные данные
    response = endpoint.register(payload)
    data = response.json()
    assert data["user"]["email"] == payload["email"]
    assert data["user"]["name"] == "Neko"
    assert data["user"]["age"] == payload["age"]

# Тест на регистрацию с невалидными данными (например, некорректный email, короткий пароль и т.д.)
# Ожидается ошибка 422

def test_registration_with_invalid_data(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_invalid_user_payload()  # генерируем невалидные данные
    response = endpoint.register(payload, expected_status=422)
    assert response.status_code == 422

# Тест на повторную регистрацию с тем же email
# Ожидается ошибка 422, так как пользователь уже существует

def test_registration_with_existing_email(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    endpoint.register(payload)
    response = endpoint.register(payload, expected_status=422)
    assert response.status_code == 422
    data = response.json()
    assert "fields" in data or "error" in data

# Тест на успешный логин сразу после регистрации
# Ожидается, что вернётся токен и email совпадёт

def test_login_with_valid_credentials(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    reg_response = endpoint.register(payload)
    assert reg_response.status_code == 200, reg_response.text
    response = endpoint.login({"email": payload["email"], "password": payload["password"]})
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert data["user"]["email"] == payload["email"]

# Тест на логин с несуществующим пользователем
# Ожидается ошибка 422

def test_login_with_invalid_credentials(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    response = endpoint.login({"email": payload["email"], "password": payload["password"]}, expected_status=422)
    assert response.status_code == 422
    data = response.json()
    assert "fields" in data or "error" in data

# Тест на логин с неправильным паролем
# Ожидается ошибка 422

def test_login_with_wrong_password(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    endpoint.register(payload)
    response = endpoint.login({"email": payload["email"], "password": "wrongpass"}, expected_status=422)
    assert response.status_code == 422
    data = response.json()
    assert "fields" in data or "error" in data

# Smoke-тест на регистрацию пользователя (быстрая проверка работоспособности /auth/register)
@pytest.mark.smoke
def test_smoke_auth_register(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    response = endpoint.register(payload)
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert "token" in data

# Smoke-тест на логин пользователя (быстрая проверка работоспособности /auth/login)
@pytest.mark.smoke
def test_smoke_auth_login(api_client, base_url):
    endpoint = AuthEndpoint(api_client, base_url)
    payload = generate_valid_user_payload()
    endpoint.register(payload)
    response = endpoint.login({"email": payload["email"], "password": payload["password"]})
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert "token" in data
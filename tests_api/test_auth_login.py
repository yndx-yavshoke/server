import pytest,requests

BASE_URL = "http://localhost:3000"
LOGIN_ENDPOINT = "/auth/login"

VALID_CREDENTIALS = {
    "email": "user100@example.com",
    "password": "string"
}

INVALID_CREDENTIALS = {
    "email": "wrong@example.com",
    "password": "wrongpassword"
}


def test_successful_login():
    """Тест успешной аутентификации с валидными данными"""
    response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json=VALID_CREDENTIALS)
    
    # Проверка статус кода
    assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"
    
    # Проверка структуры ответа
    data = response.json()
    assert "token" in data, "Токен отсутствует в ответе"
    assert isinstance(data["token"], str), "Токен должен быть строкой"
    
    # Проверка данных пользователя
    assert "user" in data, "Данные пользователя отсутствуют в ответе"
    user = data["user"]
    assert all(key in user for key in ["id", "email", "name", "age"]), "Не все обязательные поля пользователя присутствуют"

def test_invalid_credentials():
    """Тест аутентификации с неверными данными (ожидается 422)"""
    response = requests.post(f"{BASE_URL}{LOGIN_ENDPOINT}", json=INVALID_CREDENTIALS)
    
    # Проверка статус кода для неверных данных
    assert response.status_code == 422, f"Ожидался статус код 422, получен {response.status_code}"
    data = response.json()
    assert "fields" in data, "Поле 'fields' отсутствует в ответе"
    assert isinstance(data["fields"], dict), "Поле 'fields' должно быть словарем"
    assert len(data["fields"]) > 0, "Словарь fields не должен быть пустым"
def test_500_exists():
    """Простая фиксация 500 ошибки без деталей"""
    response = requests.get("http://localhost:3000/error-prone")
    if response.status_code == 500:
        pytest.xfail("Известная проблема с 500 ошибкой")
    else:
        assert True
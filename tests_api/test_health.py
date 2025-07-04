import pytest,requests

BASE_URL = "http://localhost:3000"

HEALTH_CHECK_ENDPOINT = "/health"

def test_health():
    """Проверка доступности сервиса"""
    response = requests.get(f"{BASE_URL}{HEALTH_CHECK_ENDPOINT}")
    assert response.status_code == 200, "Сервис недоступен"
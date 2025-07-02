import requests, pytest
from endpoints.health_endpoint import HealthEndpoint

# Тест на успешный health-check сервера (ожидается статус 200 и статус ok)
def test_health_status_ok(api_client, base_url):
    endpoint = HealthEndpoint(api_client, base_url)
    response = endpoint.check_health()
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"

# Тест на health-check по несуществующему URL (ожидается 404)
def test_health_check_with_invalid_url(api_client, base_url):
    invalid_url = f"{base_url}/invalid"
    response = api_client.get(invalid_url)
    assert response.status_code == 404

# Smoke-тест на health-check (быстрая проверка работоспособности)
@pytest.mark.smoke
def test_health_check_smoke(api_client, base_url):
    endpoint = HealthEndpoint(api_client, base_url)
    response = endpoint.check_health()
    assert response.status_code == 200

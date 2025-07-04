import requests

BASE_URL = "http://localhost:3000"


def test_health_server():
    #проверяем доступность сервера
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.content
import requests
from config import BASE_URL

# Тест на проверку работоспособности API
def test_health():
    response = requests.get(f'{BASE_URL}/health')
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}, тело: {response.text}"
    )

# Тест на проверку несуществующего пути
def test_health_wrong_path():
    response = requests.get(f'{BASE_URL}/healthz')
    assert response.status_code == 404, (
        f"Ожидался 404, получен {response.status_code}, тело: {response.text}"
    )

import requests


def test_health_check(api_base_url):
    """Проверка что API работает"""
    response = requests.get(f"{api_base_url}/health")
    assert response.status_code == 200


def test_api_responds_quickly(api_base_url):
    """Проверка что API отвечает быстро"""
    import time
    start_time = time.time()
    
    response = requests.get(f"{api_base_url}/health")
    
    end_time = time.time()
    response_time = end_time - start_time
    
    assert response.status_code == 200
    assert response_time < 1.0  # Должен отвечать меньше чем за секунду
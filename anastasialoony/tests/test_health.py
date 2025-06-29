import requests

def test_health():
    response = requests.get('http://localhost:3000/health')
    assert response.status_code == 200 

def test_health_wrong_path():
    response = requests.get('http://localhost:3000/healthz')
    assert response.status_code == 404

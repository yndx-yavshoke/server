import requests

URL = "http://localhost:3000"  

def test_exists_registered():
    response = requests.post(f"{URL}/exist", json={"email": "registered@example.com"}) # зарегистрированный пользователь
    
    assert response.status_code == 200
    assert response.json() == {"exist": True}

def test_exists_unregistered():
    response = requests.post(f"{URL}/exist", json={"email": "unregistred@example.com"}) # незарегистрированный пользователь
    
    assert response.status_code == 200
    assert response.json() == {"exist": False}


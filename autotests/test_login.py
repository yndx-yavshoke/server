import requests

URL = "http://localhost:3000"  

def test_login_as_registed_user():

    payload = {
  "email": "registered@example.com",
  "password": "123456"
}
    response = requests.post(f"{URL}/auth/login", json=payload) # зарегистрированный пользователь
    
    assert response.status_code == 200   # код ответа = 200

    response_data = response.json()      # cохранение в формате json
    user_data = response_data["user"]    # сохранение словаря user в user_data

    assert isinstance(response_data["token"], str)      # token должен быть string 
    assert isinstance(user_data, dict)                  # user должен быть dictionary
    assert isinstance(user_data["id"], int)             # user должен быть integer
    assert isinstance(user_data["email"], str)          # email должен быть string
    assert isinstance(user_data["name"], str)           # name должен быть string
    assert isinstance(user_data["age"], int)            # age должен быть integer

def test_login_with_invalid_credentials():

    payload = {
  "email": "registered@example.com",
  "password": "pass"
}
    response = requests.post(f"{URL}/auth/login", json=payload) # неверные креды
    
    assert response.status_code == 422   # код ответа = 422


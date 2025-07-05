import requests, time

BASE_URL = "https://api.yavshok.ru"

def test_exist_positive():
    data =  {"email": "test@yandex.ru"}
    response = requests.post(f"{BASE_URL}/exist", json=data)
    assert response.status_code == 200
    assert response.json()["exist"] == True

def test_exist_negative():
    data =  {"email": "sovsemnet0e0s0t@yandex.ru"}
    response = requests.post(f"{BASE_URL}/exist", json=data)
    assert response.status_code == 200
    assert response.json()["exist"] == False

def test_login_positive():
    data = {"email": "test0@yandex.ru", "password": "123456"}
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert "token" in json_data

def test_login_negative():
    data = {"email": "test0@yandex.ru", "password": "654321"}
    response = requests.post(f"{BASE_URL}/auth/login", json=data)
    assert response.status_code == 422
    json_data = response.json()
    assert "token" not in json_data

def change_name_and_check(new_name): #функция для смены имени и проверки
    # логинимся
    login_data = {"email": "test0@yandex.ru", "password": "123456"}
    login_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    assert login_response.status_code == 200
    token = login_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # генерим новое имя 
    name_data = {"name": new_name}

    # смена имени
    response = requests.patch(f"{BASE_URL}/user/name", json=name_data, headers=headers)
    assert response.status_code == 200
    
    # проверяем через /user/me
    profile_response = requests.get(f"{BASE_URL}/user/me", headers=headers)
    assert profile_response.status_code == 200
    assert profile_response.json()["user"]["name"] == new_name

def test_name_ru_letters():
    new_name = f"Котик_{int(time.time())}"
    change_name_and_check(new_name)

def test_name_en_letters():
    new_name = f"Cat_{int(time.time())}"
    change_name_and_check(new_name)

def test_name_special_characters():
    new_name = f"Котик_{int(time.time())}"
    change_name_and_check(new_name)
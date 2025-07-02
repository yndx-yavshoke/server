import requests
import random
from functions import generate_valid_email, generate_valid_password, url

def test_auth_positive():
    
    register_url = url + "/auth/register"
    email = generate_valid_email()
    password = generate_valid_password()
    age = random.randint(0, 99) 
    
    register_payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    register_response = requests.post(register_url, json=register_payload)
    

    assert register_response.status_code in (200, 201), \
        f"Registration failed: {register_response.text}"
    
    # успешная авторизация
    login_url = url+ "/auth/login"
    login_payload = {
        "email": email,
        "password": password
    }
    
    login_response = requests.post(login_url, json=login_payload)
    
    
    assert login_response.status_code == 200, \
        f"Login failed: {login_response.text}"
    
    response_data = login_response.json()
    assert "token" in response_data, "Token missing in response"


def test_auth_wrong_password():
    register_url = url + "/auth/register"
    email = generate_valid_email()
    password = generate_valid_password()
    age = random.randint(0, 99) 
    
    register_payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    register_response = requests.post(register_url, json=register_payload)
    

    assert register_response.status_code in (200, 201), \
        f"Registration failed: {register_response.text}"
    
    # авторизация с неверным паролем для данного логина
    login_url = url+ "/auth/login"
    login_payload = {
        "email": email,
        "password": "qwerty123"
    }
    
    login_response = requests.post(login_url, json=login_payload)
    
    
    assert login_response.status_code == 422


def test_auth_no_exist():
    login_url = url+"/auth/login"
    email = generate_valid_email()
    password = generate_valid_password()

    # авторизация с незергистрированной почтой
    login_payload = {
        "email": email,
        "password": "qwerty123" }
    
    login_response = requests.post(login_url, json=login_payload)
    
    
    assert login_response.status_code == 422
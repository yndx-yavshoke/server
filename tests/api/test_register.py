import random
import requests
import string

REGISTER_URL = "http://localhost:3000/auth/register"

def test_user_register():
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = "Qwerty123"
    age = random.randint(0, 99)

    payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    request = requests.post(REGISTER_URL, json = payload)
    assert request.status_code == 200

    data = request.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == email
    assert data["user"]["age"] == age

def test_registered_user():
    email = "v@removespread.ru"
    password = "Qwerty123"
    age = "21"

    payload = {
        "email": email,
        "password": password,
        "age": age
    }

    request = requests.post(REGISTER_URL, json = payload)
    assert request.status_code == 422

def test_short_pass_register():
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = "11"
    age = 21

    payload = {
        "email": email,
        "password": password,
        "age": age,
    }

    request = requests.post(REGISTER_URL, json = payload)
    assert request.status_code == 422

def test_long_pass_register():
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=70)),
    age = 21

    payload = {
        "email": email,
        "password": password,
        "age": age,
    }

    request = requests.post(REGISTER_URL, json = payload)
    assert request.status_code == 422
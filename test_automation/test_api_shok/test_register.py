# tests for registration, POST auth/registr

import requests
import random

BASE_URL = "http://localhost:3000"

def test_register_new_user():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    age = random.randint(0, 99)
    data = {
        "email": email,
        "password": "Test123456",
        "age": age
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert "user" in body
    assert body["user"]["email"] == email

def test_register_existing_user():
    data = {
        "email": "molodoy@gmail.com",
        "password": "12345678",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

def test_incorrect_lenght_password_insert():
    data = {
        "email": 'newuserqweqweasdazxc@example.com',
        "password": "1234",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

# Локальное API по какой-то причине разрешает пробелы в пароле
# на проде такое не работало
def test_password_nospace_insert():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    data = {
        "email": email,
        "password": "123 456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

def test_passwordwith_specialsymbols_insert():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    data = {
        "email": email,
        "password": "@!#!$!$%!!(&@#59712912579",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200

def test_password_onlyspecialsymbols_insert():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    data = {
        "email": email,
        "password": "@!#$%^$!&@$@!$^",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200

def test_age_zero_insert():
    email = f"newuser{random.randint(100000, 999999)}@example.com"
    data = {
        "email": email,
        "password": "123456ererer",
        "age": 0
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200

def test_age_minusone_insert():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    age = "-1"
    data = {
        "email": email,
        "password": "123456",
        "age": age,
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

def test_age_letters_insert():
    email = f"newuser{random.randint(10000, 99999)}@example.com"
    age = "двадцать"
    data = {
        "email": email,
        "password": "123456",
        "age": age,
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

def test_age_99_insert():
    email = f"newuse{random.randint(10000, 99999)}@example.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 99
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200

def test_age_100_insert():
    email = f"newuse{random.randint(10000, 99999)}@example.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 100
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422

def test_incorrect_email_nodot_insert():
    email = "0@mailcom"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_email_nolocalpart_insert():
    email = "1234@"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_email_nounderscore_insert():
    email = "1234@mai_l.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_email_nocyrillic_insert():
    email = "кириллица@почта.рф"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_email_nofirstpart_insert():
    email = "@mail.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_space_beforeat_email_insert():
    email = "a b@mail.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_spaceafterat_email_insert():
    email = "ab@mail .com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_incorrect_lenght_email_insert():
    email = f"{'a'*51}@mail.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 422
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()

def test_50symbols_lenght_email_insert():
    email = f"{'a'*50}@mail.com"
    data = {
        "email": email,
        "password": "123456",
        "age": 22
    }
    response = requests.post(f"{BASE_URL}/auth/register", json=data)

    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp.get("type") == "validation"
    assert "found" in json_resp
    assert "email" in json_resp["found"]
    # assert "fields" in response.json()
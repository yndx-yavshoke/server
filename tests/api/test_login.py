import requests
import random

# Я решил полностью переписать эти тесты в час ночи
# Не стал намеренно использовать Claude / Cursor / ChatGPT / Grok etc. 
# Потому что уж лучше я научусь так, чем вообще не научусь и потом буду сосать бибу :с
# Какашки можно закидывать в ТГ - @removespread
def test_user_login():
    REGISTER_URL = "http://localhost:3000/auth/register"
    LOGIN_URL = "http://localhost:3000/auth/login"
    email = f"Vic{random.randint(1, 1000)}test@removespread.ru"
    password = "Qwerty123"
    payload = {
        "email": email,
        "password": password,
        "age": 21
    }

    response = requests.post(REGISTER_URL, json = payload)
    assert response.status_code == 200
    
    another_payload = {
        "email": email,
        "password": password
    }

    response = requests.post(LOGIN_URL, json = payload)
    assert response.status_code == 200

    data = response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == email

# апдейт от 1:29
# я полчаса потратил на фикс импортов
# спасибо venv и работе с пакетами
# по хорошему все УРЛы нужно перекинуть в другой файл

def test_nonexist_userlogon():
    LOGIN_URL = "http://localhost:3000/auth/login"
    email = "notexist@removespread.ru"
    password = "Qwerty123"

    payload = {
        "email": email,
        "password": password
    }
    request = requests.post(LOGIN_URL, json = payload)
    assert request.status_code == 422
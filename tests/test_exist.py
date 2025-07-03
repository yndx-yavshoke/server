import pytest
import requests

from tests.variables.const import EXIST_URL

def test_exist_user():
    url = EXIST_URL
    payload = {
        "email": "test@removespread.ru"
    }
    response = requests.post(url, json = payload)

    # Все то, что выше - нужно вынести в какую-нибудь функцию
    # Нужно рефакторить, понимание придет со временем
    assert response.status_code == 200
    data = response.json
    assert data["exist"] is True

def test_exist_user():
    url = EXIST_URL
    payload = {
        "email": "imnotexist@removespread.ru"
    }

    response = requests.post(url, json = payload)
    assert response.status_code == 200
    data = response.json
    assert data["exist"] is False

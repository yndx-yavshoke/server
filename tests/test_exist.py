import pytest
import requests

from tests.variables.const import EXIST_URL
from tests.api.exist import exist

def test_exist_user():
    request = exist("v@removespread.ru")

    assert request.status_code == 200

    data = request.json()
    assert "exist" in data and data["exist"] is True

def test_not_exist_user():
    request = exist("notexist@removespread.ru")

    assert request.status_code == 200

    data = request.json()
    assert "exist" in data and data["exist"] is False
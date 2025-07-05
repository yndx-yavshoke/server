import pytest
from utils.data_generators import generate_email

@pytest.fixture
def shock_endpoint(client):
    return client

def test_api_should_exist(shock_endpoint, api_username):
    """
    Тест проверки существования пользователя с существующим email.
    """
    response: dict = shock_endpoint.check_exist(api_username)
    assert response["status_code"] == 200
    assert response["body"]["exist"] is True

def test_api_should_not_exist(shock_endpoint):
    """
    Тест проверки существования пользователя с несуществующим email.
    """
    response: dict = shock_endpoint.check_exist(generate_email())
    assert response["status_code"] == 200
    assert response["body"]["exist"] is False

def test_api_should_not_exist_with_null_value(shock_endpoint):
    """
    Тест проверки существования пользователя с null значением email.
    """
    response: dict = shock_endpoint.check_exist(None)
    assert response["status_code"] == 422


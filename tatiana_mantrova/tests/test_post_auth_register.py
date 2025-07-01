import pytest
from api_client.exceptions import ApiException

def test_register_valid_user(api, random_user):
    """Регистрация пользователя со всеми заполненными полями"""

    response = api.post_auth_register_with_http_info(post_auth_register_request = random_user)
    
    assert response.data.user.email == random_user.email
    assert response.status_code == 200

def test_register_user_without_email(api, random_user):
    """Регистрация пользователя c пустым полем email"""

    try:
        random_user.email = ""
        api.post_auth_register(post_auth_register_request = random_user)
    except ApiException as e:
        assert e.status == 422

def test_register_valid_user_without_age(api, random_user):
    """Регистрация пользователя c пустым полем Возраст"""

    try:
        random_user.age = None
        api.post_auth_register(post_auth_register_request = random_user)
    except ApiException as e:
        assert e.status == 422
        
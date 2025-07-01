import pytest
from api_client.models import PostAuthLoginRequest
from api_client.exceptions import ApiException

def test_login_existed_user(api, random_user):
    """Логин зарегистрированного пользователя"""
    
    api.post_auth_register(post_auth_register_request = random_user)

    model = PostAuthLoginRequest(email = random_user.email, password = random_user.password)
    response = api.post_auth_login_with_http_info(post_auth_login_request = model) 

    assert response.status_code == 200

def test_login_not_existed_user(api, random_user):
    """Логин незарегистрированного пользователя"""
    try:
        model = PostAuthLoginRequest(email = random_user.email, password = random_user.password)
        api.post_auth_login(post_auth_login_request = model)
    except ApiException as e:
        assert e.status == 422

def test_login_user_without_email(api, random_user):
    """Логин пользователя без почты"""
    try:
        model = PostAuthLoginRequest(email = "", password = random_user.password)
        api.post_auth_login(post_auth_login_request = model)
    except ApiException as e:
        assert e.status == 422

def test_login_user_without_password(api, random_user):
    """Логин пользователя без почты"""
    try:
        model = PostAuthLoginRequest(email = random_user.email, password = "")
        api.post_auth_login(post_auth_login_request = model)
    except ApiException as e:
        assert e.status == 422

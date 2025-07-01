import pytest
from api_client.models import PostExistRequest

def test_user_exist(api, random_user):
    """Зарегистрированный пользователь в ШОКе"""

    api.post_auth_register(post_auth_register_request = random_user)
    
    model = PostExistRequest(email = random_user.email)
    response = api.post_exist(post_exist_request = model)

    assert response.exist == True
    
def test_user_not_exist(api, random_user):
    """Незарегистрированный пользователь не в ШОКе"""
    
    model = PostExistRequest(email = random_user.email)
    response = api.post_exist(post_exist_request = model)

    assert response.exist == False
    
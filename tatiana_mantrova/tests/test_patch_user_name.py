import pytest
from api_client.models.patch_user_name_request import PatchUserNameRequest

def test_name_change_with_auth_fixture(authenticated_api):
    """Изменение имени пользователя"""

    new_name = "New_name"
    model = PatchUserNameRequest(name = new_name)
    response = authenticated_api.patch_user_name(patch_user_name_request = model)
    
    assert response.user.name == new_name

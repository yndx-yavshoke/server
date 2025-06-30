import pytest
from utils.test_helpers import assert_user_response_structure
from src.client.endpoints.user import UserEndpoint
from utils.testdata import user_name_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def user_endpoint(client):
    return UserEndpoint(client)

@pytest.mark.parametrize("new_name,expected_status_code", user_name_cases)
def test_api_name(user_endpoint, api_username, api_password, new_name, expected_status_code):
    new_name = get_test_value(new_name, api_username=api_username)
    response = user_endpoint.change_name(new_name, api_username, api_password)
    assert response["status_code"] == expected_status_code
    if expected_status_code == 200:
        assert response["body"]["user"]["name"] == new_name

def test_api_user(user_endpoint, api_username, api_password):
    response = user_endpoint.get_current_user(api_username, api_password)
    assert_user_response_structure(response, api_username)
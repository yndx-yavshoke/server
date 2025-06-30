import pytest
from utils.test_helpers import assert_auth_response_structure
from client.endpoints.auth import AuthEndpoint
from utils.testdata import registration_cases, auth_login_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def auth_endpoint(client):
    return AuthEndpoint(client)

@pytest.mark.parametrize("email,password,age,expected_status_code", registration_cases)
def test_api_registration(auth_endpoint, email, password, age, expected_status_code, api_username):
    email = get_test_value(email, api_username=api_username, api_password=None)
    password = get_test_value(password, api_username=api_username, api_password=None)
    age = get_test_value(age)
    response = auth_endpoint.register(email, password, age)
    assert response["status_code"] == expected_status_code
    if expected_status_code == 200:
        assert_auth_response_structure(response, email, age)

@pytest.mark.parametrize("email,password,expected_status_code", auth_login_cases)
def test_api_login(auth_endpoint, api_username, api_password, email, password, expected_status_code):
    email = get_test_value(email, api_username=api_username, api_password=api_password)
    password = get_test_value(password, api_username=api_username, api_password=api_password)
    response = auth_endpoint.login(email, password)
    assert response["status_code"] == expected_status_code
    if expected_status_code == 200:
        assert_auth_response_structure(response, email)
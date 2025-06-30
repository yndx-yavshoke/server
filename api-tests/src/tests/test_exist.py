import pytest
from utils.testdata import exist_cases
from utils.test_value_factory import get_test_value

@pytest.fixture
def shock_endpoint(client):
    return client

@pytest.mark.parametrize("email,expected_exist,expected_status_code", exist_cases)
def test_api_exist(shock_endpoint, api_username, email, expected_exist, expected_status_code):
    test_email = get_test_value(email, api_username=api_username)
    response = shock_endpoint.check_exist(test_email)
    assert response["status_code"] == expected_status_code
    if expected_status_code == 200:
        assert response["body"]["exist"] is expected_exist

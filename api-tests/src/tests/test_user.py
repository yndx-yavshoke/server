import pytest
from utils.assertion_helpers import assert_user_response_structure
from utils.data_generators import generate_name, generate_string
from client.endpoints.user import UserEndpoint

@pytest.fixture
def user_endpoint(client) -> UserEndpoint:
    return UserEndpoint(client)

@pytest.mark.parametrize(
    "new_name",
    [
        generate_name(),
        "'; DROP TABLE users; --",
        generate_name(),
        generate_name(language="ru_RU"),
    ]
)
def test_api_should_change_name(
    user_endpoint: UserEndpoint,
    api_username: str,
    api_password: str,
    new_name: str
) -> None:
    """
    Тест успешной смены имени пользователя.
   """
    response: dict = user_endpoint.change_name(new_name, api_username, api_password)
    assert response["status_code"] == 200
    assert response["body"]["user"]["name"] == new_name


@pytest.mark.parametrize(
    "new_name",
    [
        "",
        None,
        generate_string(256)
    ]
)
def test_api_should_not_change_name(
    user_endpoint: UserEndpoint,
    api_username: str,
    api_password: str,
    new_name: str
) -> None:
    """
    Тест отклонения смены имени с невалидными данными.
    """
    response: dict = user_endpoint.change_name(new_name, api_username, api_password)
    assert response["status_code"] == 422

def test_api_should_get_user(
    user_endpoint: UserEndpoint,
    api_username: str,
    api_password: str
) -> None:
    """
    Тест получения данных текущего пользователя.
    """
    response: dict = user_endpoint.get_current_user(api_username, api_password)
    assert_user_response_structure(response)
    assert response["body"]["user"]["email"] == api_username
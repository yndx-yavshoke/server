import pytest
from utils.assertion_helpers import assert_auth_response_structure
from client.endpoints.auth import AuthEndpoint
from utils.data_generators import generate_email, generate_age, generate_password, generate_fixed_email

@pytest.fixture
def auth_endpoint(client) -> AuthEndpoint:
    return AuthEndpoint(client)

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        (generate_email(), generate_password(), generate_age()),
        (generate_fixed_email(5), generate_password(5), generate_age()),
        (generate_fixed_email(50), generate_password(), 0),
        (generate_email(), generate_password(20), 99)
    ],
)
def test_api_should_register(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age: int
) -> None:
    """
    Тест успешной регистрации пользователя.
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 200
    assert_auth_response_structure(response)
    assert response["body"]["user"]["email"] == email
    response_age = response["body"]["user"].get("age")
    if age == 0:
        assert response_age in (None, 0)
    else:
        assert response_age == age

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        (generate_email(), generate_password(), 100),
        (generate_email(), generate_password(), -1),
        (generate_email(), generate_password(), "two"),
    ],
)
def test_api_should_not_register_with_invalid_age(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age
) -> None:
    """
    Тест отклонения регистрации с возрастом вне допустимого диапазона (0-99).
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 422

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        ("a@bc", generate_password(), generate_age()),
        (f" {generate_email()}", generate_password(), generate_age()),
        ("test@example#com", generate_password(), generate_age()),
    ],
)
def test_api_should_not_register_with_invalid_email(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age: int
) -> None:
    """
    Тест отклонения регистрации с невалидным email.
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 422

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        (generate_email(), generate_password(4), generate_age()),
        (generate_email(), generate_password(21), generate_age()),
    ],
)
def test_api_should_not_register_with_invalid_password_length(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age: int
) -> None:
    """
    Тест отклонения регистрации с длиной пароля 4 или 21 символ.
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 422

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        ("", generate_password(), generate_age()),
        (generate_email(), "", generate_age()),
        (generate_email(), generate_password(), ""),
        (None, generate_password(), generate_age()),
        (generate_email(), None, generate_age()),
        (generate_email(), generate_password(), None),
    ],
)
def test_api_should_not_register_with_empty_or_null_values(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age: int
) -> None:
    """
    Тест отклонения регистрации с пустыми или null значениями.
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 422

@pytest.mark.parametrize(
    ('email', 'password', 'age'),
    [
        ("; DROP TABLE users; --", generate_password(), generate_age()),
        (generate_email(), "; DROP TABLE users; --", generate_age()),
    ],
)
def test_api_should_not_register_with_sql_injection(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str,
    age: int
) -> None:
    """
    Тест отклонения регистрации с SQL-инъекциями.
    """
    response: dict = auth_endpoint.register(email, password, age)
    assert response["status_code"] == 422

def test_api_should_not_register_with_the_same_email(
    auth_endpoint: AuthEndpoint,
    api_username: str,
    api_password: str
) -> None:
    """
    Тест отклонения регистрации с уже существующим email.
    """
    response: dict = auth_endpoint.register(api_username, api_password, generate_age())
    assert response["status_code"] == 422

def test_api_should_login(
    auth_endpoint: AuthEndpoint,
    api_username: str,
    api_password: str
) -> None:
    """
    Тест успешного входа в систему.
    """
    response: dict = auth_endpoint.login(api_username, api_password)
    assert response["status_code"] == 200
    assert_auth_response_structure(response)
    assert response["body"]["user"]["email"] == api_username

@pytest.mark.parametrize(
    ('email', 'password'),
    [
        ("api_username", generate_password()),
        (generate_email(), generate_password()),
        ("", generate_password()),
        (generate_email(), ""),
    ]
)
def test_api_should_not_login(
    auth_endpoint: AuthEndpoint,
    email: str,
    password: str
) -> None:
    """
    Тест отклонения входа с невалидными данными: неправильным паролем, неправильным логином, пустыми полями.
    """
    response: dict = auth_endpoint.login(email, password)
    assert response["status_code"] == 422
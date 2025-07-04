import pytest
from faker import Faker
import requests
import logging
from utils.config import BASE_URL

fake = Faker("ru_RU")

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    fh = logging.FileHandler("test_logs.log", mode='w', encoding='utf-8')
    sh = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)

    logger.info("=== Starting test session ===")
    yield
    logger.info("=== Finishing test session ===")

@pytest.fixture
def user_credentials():
    return {
        "email": fake.unique.email(),
        "password": fake.password(length=8),
        "age": fake.random_int(min=0, max=99)
    }

@pytest.fixture
def register_user(user_credentials):
    response = requests.post(f"{BASE_URL}/auth/register", json=user_credentials)
    assert response.status_code in [200, 422], "User registration failed"
    return user_credentials

@pytest.fixture
def auth_token(register_user):
    login_response = requests.post(f"{BASE_URL}/auth/login", json=register_user)
    assert login_response.status_code == 200, "Login failed"
    return login_response.json()["token"]

@pytest.fixture
def new_user_name():
    return fake.first_name()

@pytest.fixture
def not_exist_email():
    return fake.unique.email()
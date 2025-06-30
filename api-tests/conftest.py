import pytest
from dotenv import load_dotenv
import os
from src.client.api_client import ApiClient

load_dotenv()

@pytest.fixture(scope="session")
def api_base_url():
    url = os.getenv('API_BASE_URL')
    if not url:
        raise RuntimeError("API_BASE_URL is not set in environment variables")
    return url

@pytest.fixture(scope="session")
def api_username():
    username = os.getenv('API_USERNAME')
    if not username:
        raise RuntimeError("API_USERNAME is not set in environment variables")
    return username

@pytest.fixture(scope="session")
def api_password():
    password = os.getenv('API_PASSWORD')
    if not password:
        raise RuntimeError("API_PASSWORD is not set in environment variables")
    return password

@pytest.fixture
def client(api_base_url):
    return ApiClient(api_base_url)

import pytest
from dotenv import load_dotenv
import os
from src.client.api_client import ApiClient

load_dotenv()

@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv('API_BASE_URL')

@pytest.fixture(scope="session")
def api_username():
    return os.getenv('API_USERNAME')

@pytest.fixture(scope="session")
def api_password():
    return os.getenv('API_PASSWORD')

@pytest.fixture
def client(api_base_url):
    return ApiClient(api_base_url)

@pytest.fixture(autouse=True)
def print_docstring(request):
    doc = request.function.__doc__
    if doc:
        print(f"\n{doc.strip()}\n")

import pytest
import uuid
import os
import random
from dotenv import load_dotenv
from api_client import ApiClient, Configuration
from api_client.models.post_auth_register_request import PostAuthRegisterRequest

load_dotenv()

@pytest.fixture
def api_config():
    """Фикстура конфигурации API"""
    base_url = os.getenv("API_BASE_URL")

    if not base_url:
        raise ValueError("Задайте API_BASE_URL в .env")

    config = Configuration()
    config.host = base_url
    return config

@pytest.fixture
def api(api_config):
    """Фикстура для API"""
    from api_client.api.default_api import DefaultApi
    return DefaultApi(ApiClient(api_config))

@pytest.fixture
def authenticated_api(api, random_user):
    """Фикстура для API клиента c токеном"""
    reg_response = api.post_auth_register(post_auth_register_request = random_user)
    api.api_client.configuration.access_token = reg_response.token
    return api

@pytest.fixture
def random_user():
    """Фикстура для создания модели случайного пользователя"""
    return PostAuthRegisterRequest(
        email = f"user_{uuid.uuid4().hex}@example.com",
        password = "TestPassword123",
        age = random.randrange(100)
    )

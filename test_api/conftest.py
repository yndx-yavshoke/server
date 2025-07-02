import pytest
import requests
import logging
from utils.base_endpoint import BaseEndpoint
from utils.jwt_handler import JWTHandler
from endpoints.health_endpoint import HealthEndpoint

logger = logging.getLogger(__name__)

# Фикстура для базового URL API (используется во всех тестах)
@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"

# Фикстура для получения JWT токена (использует JWTHandler)
@pytest.fixture(scope="session")
def jwt_token(base_url):
    jwt_handler = JWTHandler(base_url)
    return jwt_handler.get_jwt_token()

# Фикстура для создания сессии requests с JWT авторизацией
@pytest.fixture(scope="session")
def api_client(base_url, jwt_token):
    with requests.Session() as session:
        session.headers.update({
            'Authorization': f'Bearer {jwt_token}',
            'Content-Type': 'application/json'
        })
        logger.info("Создана сессия с JWT аутентификацией")
        yield session
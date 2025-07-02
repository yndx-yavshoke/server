import pytest
from utils.base_endpoint import BaseEndpoint
from utils.data_generator import generate_valid_user_payload, generate_invalid_user_payload

class AuthEndpoint(BaseEndpoint):
    def __init__(self, session, base_url):
        super().__init__(session, base_url)
        self.register_path = "/auth/register"  # путь для регистрации
        self.login_path = "/auth/login"        # путь для логина

    def register(self, payload=None, expected_status=200): # регистрация нового пользователя
        # Временно убираем заголовок Authorization, если он есть
        old_auth = self.session.headers.pop('Authorization', None)
        try:
            if payload is None:
                payload = generate_valid_user_payload()  # генерируем валидные данные
            return self.post(self.register_path, payload, expected_status)
        finally:
            # Возвращаем заголовок Authorization, если он был
            if old_auth is not None:
                self.session.headers['Authorization'] = old_auth

    def login(self, payload=None, expected_status=200): # аутентификация пользователя
        # Временно убираем заголовок Authorization, если он есть
        old_auth = self.session.headers.pop('Authorization', None)
        try:
            if payload is None:
                payload = {"email": "test@example.com", "password": "valid123"}
            return self.post(self.login_path, payload, expected_status)
        finally:
            # Возвращаем заголовок Authorization, если он был
            if old_auth is not None:
                self.session.headers['Authorization'] = old_auth

# Фикстура для использования в тестах
@pytest.fixture
def auth_endpoint(api_client, base_url):
    return AuthEndpoint(api_client, base_url)
import pytest
from utils.base_endpoint import BaseEndpoint
from utils.data_generator import generate_valid_user_payload

# Класс для работы с эндпоинтом /exist (проверка существования пользователя по email)
class ExistEndpoint(BaseEndpoint):
    def __init__(self, session, base_url):
        super().__init__(session, base_url)
        self.exist_path = "/exist"  # путь для проверки

    def check_exist(self, payload=None, expected_status=200): # проверка существования пользователя по email
        if payload is None:
            payload = {"email": generate_valid_user_payload()["email"]}
        return self.post(self.exist_path, payload, expected_status)

# Фикстура для использования в тестах
@pytest.fixture
def exist_endpoint(api_client, base_url):
    return ExistEndpoint(api_client, base_url)
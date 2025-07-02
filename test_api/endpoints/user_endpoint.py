import pytest
from utils.base_endpoint import BaseEndpoint
from utils.data_generator import generate_name_update_payload, generate_invalid_name_update_payload

# Класс для работы с пользовательскими эндпоинтами (/user/me, /user/name)
class UserEndpoint(BaseEndpoint):
    def __init__(self, session, base_url):
        super().__init__(session, base_url)
        self.me_path = "/user/me"      # путь для получения данных пользователя
        self.name_path = "/user/name"  # путь для обновления имени

    def get_me(self, expected_status=200): # получение данных текущего пользователя
        return self.get(self.me_path, expected_status)

    def update_name(self, payload=None, expected_status=200): # обновление имени пользователя
        if payload is None:
            payload = generate_name_update_payload()
        return self.patch(self.name_path, payload, expected_status)

# Фикстура для использования в тестах
@pytest.fixture
def user_endpoint(api_client, base_url):
    return UserEndpoint(api_client, base_url)
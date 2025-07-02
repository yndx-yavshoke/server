import pytest
from utils.base_endpoint import BaseEndpoint

# Класс для работы с эндпоинтом /health
class HealthEndpoint(BaseEndpoint):
    def __init__(self, session, base_url):
        super().__init__(session, base_url)
        self.health_path = "/health"  # путь для health-check

    def check_health(self, expected_status=200): # проверка состояния сервера
        return self.get(self.health_path, expected_status=expected_status)
import requests
import logging

logger = logging.getLogger(__name__)

# Класс для получения и хранения JWT токена через эндпоинт /auth/login
class JWTHandler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def get_jwt_token(self, email="test@example.com", password="valid123"):
        """
        Получает JWT токен через эндпоинт /auth/login.
        
        :param email: Электронная почта пользователя (по умолчанию test@example.com)
        :param password: Пароль пользователя (по умолчанию valid123)
        :return: JWT токен
        """
        payload = {
            "email": email,
            "password": password
        }

        try:
            response = requests.post(f"{self.base_url}/auth/login", json=payload)
            response.raise_for_status()
            token_data = response.json()
            self.token = token_data.get("token")
            if self.token:
                logger.info("Успешно получен JWT токен")
                return self.token
            else:
                logger.error("Токен не найден в ответе")
                raise ValueError("Токен не получен")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при получении JWT токена: {str(e)}")
            raise

    def set_token(self, token):
        """
        Устанавливает токен вручную (например, для тестов).
        
        :param token: JWT токен
        """
        self.token = token
        logger.info("Токен установлен вручную")
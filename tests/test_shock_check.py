import requests
import pytest


class TestShockCheck:
    """Тесты проверки ШОКовости (endpoint /exist)"""
    
    def test_shock_check_with_valid_email(self, api_base_url):
        """Тест проверки ШОКовости с валидным email"""
        url = f"{api_base_url}/exist"
        data = {"email": "test@example.com"}
        response = requests.post(url, json=data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "exist" in json_data
        assert isinstance(json_data["exist"], bool)
        # exist может быть True или False - это нормально
    
    def test_shock_check_with_existing_user(self, api_base_url, registered_user):
        """Тест проверки ШОКовости с зарегистрированным пользователем"""
        url = f"{api_base_url}/exist"
        data = {"email": registered_user["email"]}
        response = requests.post(url, json=data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "exist" in json_data
        assert json_data["exist"] is True  # Зарегистрированный пользователь должен существовать
    
    def test_shock_check_with_nonexistent_user(self, api_base_url):
        """Тест проверки ШОКовости с несуществующим пользователем"""
        url = f"{api_base_url}/exist"
        data = {"email": "definitely_nonexistent_user_12345@example.com"}
        response = requests.post(url, json=data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "exist" in json_data
        assert json_data["exist"] is False  # Несуществующий пользователь
    
    def test_shock_check_with_invalid_email_format(self, api_base_url):
        """Тест проверки ШОКовости с невалидным форматом email"""
        url = f"{api_base_url}/exist"
        data = {"email": "invalid-email-format"}
        response = requests.post(url, json=data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "exist" in json_data
        assert json_data["exist"] is False
    
    @pytest.mark.parametrize("invalid_email", [
        "",  # пустой email
        "just-text",  # без @
        "@domain.com",  # без пользователя
        "user@",  # без домена
        "user@domain",  # без зоны
        "user space@domain.com",  # с пробелом
    ])
    def test_shock_check_various_invalid_emails(self, api_base_url, invalid_email):
        """Тест проверки ШОКовости с различными невалидными email"""
        url = f"{api_base_url}/exist"
        data = {"email": invalid_email}
        response = requests.post(url, json=data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "exist" in json_data
        assert json_data["exist"] is False
    
    def test_shock_check_without_email_field(self, api_base_url):
        """Тест проверки ШОКовости без поля email"""
        url = f"{api_base_url}/exist"
        data = {}  # пустые данные
        response = requests.post(url, json=data)
        
        
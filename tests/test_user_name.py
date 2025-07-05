import requests
import pytest


class TestUserName:
    """Тесты изменения имени пользователя (endpoint /user/name)"""
    
    def test_change_name_with_auth(self, api_base_url, auth_token):
        """Тест успешного изменения имени с авторизацией"""
        url = f"{api_base_url}/user/name"
        headers = {"Authorization": f"Bearer {auth_token}"}
        data = {"name": "Эричка"}
        
        response = requests.patch(url, json=data, headers=headers)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "user" in json_data
        assert json_data["user"]["name"] == "Эричка"
    
    def test_change_name_without_auth(self, api_base_url):
        """Тест изменения имени без авторизации"""
        url = f"{api_base_url}/user/name"
        data = {"name": "Эричка"}
        
        response = requests.patch(url, json=data)
        assert response.status_code == 401
    
    def test_change_name_with_invalid_token(self, api_base_url):
        """Тест изменения имени с невалидным токеном"""
        url = f"{api_base_url}/user/name"
        headers = {"Authorization": "Bearer invalid_token_here"}
        data = {"name": "Эричка"}
        
        response = requests.patch(url, json=data, headers=headers)
        assert response.status_code == 401
    
    def test_change_name_empty_name(self, api_base_url, auth_token):
        """Тест изменения имени на пустое"""
        url = f"{api_base_url}/user/name"
        headers = {"Authorization": f"Bearer {auth_token}"}
        data = {"name": ""}
        
        response = requests.patch(url, json=data, headers=headers)
        assert response.status_code == 422
    
    def test_change_name_too_long(self, api_base_url, auth_token):
        """Тест изменения имени на слишком длинное"""
        url = f"{api_base_url}/user/name"
        headers = {"Authorization": f"Bearer {auth_token}"}
        data = {"name": "a" * 51}  # больше 50 символов
        
        response = requests.patch(url, json=data, headers=headers)
        assert response.status_code == 422
    
    @pytest.mark.parametrize("new_name", [
        "Анна",
        "John Smith", 
        "Мария-Петровна",
        "User123",
        "a" * 50  # максимальная длина
    ])
    def test_change_name_valid_names(self, api_base_url, auth_token, new_name):
        """Тест изменения имени на различные валидные имена"""
        url = f"{api_base_url}/user/name"
        headers = {"Authorization": f"Bearer {auth_token}"}
        data = {"name": new_name}
        
        response = requests.patch(url, json=data, headers=headers)
        
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["user"]["name"] == new_name
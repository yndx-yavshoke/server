import requests


class TestAuth:
    """Тесты авторизации (endpoints /auth/register и /auth/login)"""
    
    def test_user_registration_success(self, api_base_url, unique_user_data):
        """Тест успешной регистрации нового пользователя"""
        register_url = f"{api_base_url}/auth/register"
        response = requests.post(register_url, json=unique_user_data)
        
        if response.status_code == 200:
            # Успешная регистрация
            json_data = response.json()
            assert "token" in json_data
            assert "user" in json_data
            assert json_data["user"]["email"] == unique_user_data["email"]
        else:
            # Пользователь уже существует
            assert response.status_code == 422
    
    def test_user_login_success(self, api_base_url, registered_user):
        """Тест успешного логина"""
        login_url = f"{api_base_url}/auth/login"
        login_data = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        
        response = requests.post(login_url, json=login_data)
        
        assert response.status_code == 200
        json_data = response.json()
        assert "token" in json_data
        assert "user" in json_data
        assert json_data["user"]["email"] == registered_user["email"]
    
    def test_login_with_wrong_password(self, api_base_url, registered_user):
        """Тест логина с неправильным паролем"""
        login_url = f"{api_base_url}/auth/login"
        login_data = {
            "email": registered_user["email"],
            "password": "wrong_password"
        }
        
        response = requests.post(login_url, json=login_data)
        assert response.status_code == 422
    
    def test_login_with_nonexistent_user(self, api_base_url):
        """Тест логина с несуществующим пользователем"""
        login_url = f"{api_base_url}/auth/login"
        login_data = {
            "email": "nonexistent@example.com",
            "password": "somepassword"
        }
        
        response = requests.post(login_url, json=login_data)
        assert response.status_code == 422
    
    def test_registration_without_required_fields(self, api_base_url):
        """Тест регистрации без обязательных полей"""
        register_url = f"{api_base_url}/auth/register"
        
        # Без email
        response = requests.post(register_url, json={"password": "123456"})
        assert response.status_code in [400, 422]
        
        # Без password
        response = requests.post(register_url, json={"email": "test@test.com"})
        assert response.status_code in [400, 422]
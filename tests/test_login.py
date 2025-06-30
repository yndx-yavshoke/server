from api_client import APIClient
from services import UserService
import pytest

@pytest.mark.parametrize("email,password", [
    ("yassbar@mail.ru", "1234567"),
    ("aassbar@mail.ru", "1234567"),
    ("oassbar@mail.ru", "1234567"),
])
def test_login(email, password):
    client = APIClient("http://localhost:3000")
    user_service = UserService(client)

    profile = user_service.login_and_get_profile(email, password)

    user_data = profile.get("user")

    assert user_data is not None, f"Не удалось получить профиль пользователя для {email}"

    assert "id" in user_data, f"Нет поля id в профиле для {email}"
    assert "email" in user_data, f"Нет поля email в профиле для {email}"
    assert user_data["email"] == email, f"Email в профиле не совпадает для {email}"
    assert "name" in user_data, f"Нет поля name в профиле для {email}"
    assert "age" in user_data, f"Нет поля age в профиле для {email}"


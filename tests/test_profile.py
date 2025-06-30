from api_client import APIClient
from services import UserService

def test_update_user_name():
    client = APIClient("http://localhost:3000")
    user_service = UserService(client)

    new_name = "ngriizl"
    profile = user_service.login_and_change_name(
        "yassbar@mail.ru",
        "1234567",
        new_name
    )

    user_data = profile["user"]

    assert user_data.get("name") == new_name


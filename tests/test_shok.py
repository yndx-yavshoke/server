from api_client import APIClient
from services import ShokService

def test_shok_check_registered():
    client = APIClient("http://localhost:3000")
    shok_service = ShokService(client)

    result = shok_service.check_shok_status("oassbar@mail.ru")
    assert result["message"] == "Ты уже в ШОКе"

def test_shok_check_not_registered():
    client = APIClient("http://localhost:3000")
    shok_service = ShokService(client)

    result = shok_service.check_shok_status("notregissstered@example.com")
    assert result["message"] == "Ты ещё не в ШОКе"


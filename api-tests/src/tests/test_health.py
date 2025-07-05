def test_api_available(client):
    """
    Тест доступности API и подключения к базе данных.
    """
    response: dict = client.check_health()
    assert response["body"]["status"] == "ok"
    assert response["body"]["database"] == "connected"
def test_api_available(client):
    response = client.check_health()
    assert response["status_code"] == 200
    body = response["body"]
    assert body["status"] == "ok"
    assert body["database"] == "connected"
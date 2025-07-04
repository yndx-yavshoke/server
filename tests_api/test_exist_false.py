import requests,pytest
AUTH_CHECK_ENDPOINT = "http://localhost:3000/exist"
def test_check_autorized():
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjUsImlhdCI6MTc1MTQxNDQzMywiZXhwIjoxNzUxNTAwODMzfQ.NibD5Shu2dInt2Y8qILunxKipdNGUHg-GWPjqjiCen4"
    }
    payload = {
        "email": "user100@example.com"
    }
    response = requests.post(AUTH_CHECK_ENDPOINT,headers=headers,json=payload)
    response_json = response.json()
    assert "exist" in response_json
    assert response.status_code == 200
    assert response_json["exist"] is False
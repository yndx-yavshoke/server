# Tests for GET/health

import requests
BASE_URL = "http://localhost:3000"
#from utils.constants import BASE_URL

def test_server_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200

# def test_baseurl_islocal():
#     print(f"Current URL is: {BASE_URL}")
#     assert BASE_URL.startswith("http://localhost:3000")
import requests
import logging
from utils.config import BASE_URL

logger = logging.getLogger(__name__)

def test_login_user(register_user):
    logger.info(f"Login test started for email: {register_user['email']}")
    response = requests.post(f"{BASE_URL}/auth/login", json=register_user)
    logger.info(f"Response status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200, "Login failed"
    data = response.json()
    assert "token" in data, "Token not found in response"
    assert "user" in data, "User data missing in response"
    assert data["user"]["email"] == register_user["email"]
    logger.info("Login test passed")
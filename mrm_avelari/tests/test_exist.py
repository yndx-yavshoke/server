import requests
import logging
from utils.config import BASE_URL

logger = logging.getLogger(__name__)

def test_email_shok(register_user):
    logger.info(f"Checking if email exists: {register_user["email"]}")
    payload = {
        "email": register_user["email"]
    }
    response = requests.post(f"{BASE_URL}/exist", json=payload)
    logger.info(f"Existence check response status: {response.status_code}")
    assert response.status_code == 200, "Email existence check failed"
    data = response.json()
    assert "exist" in data, "Missing exist in response"
    assert response.json()["exist"] is True
    logger.info(f"Email {register_user["email"]} confirmed to exist")

def test_email_not_shok(not_exist_email):
    logger.info(f"Checking if non-existent email: {not_exist_email}")
    response = requests.post(f"{BASE_URL}/exist", json={"email": not_exist_email})
    logger.info(f"Existence check response status: {response.status_code}")
    assert response.status_code == 200, "Email existence check failed"
    assert response.json()["exist"] is False
    logger.info(f"Email {not_exist_email} confirmed to NOT exist")
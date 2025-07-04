import requests

from config import API_BASE_URL
from services.user import generate_unique_name


def test_login_required_edit_name(authenticated_user_headers):
    data = {
        "name": "normal name"
    }
    response = requests.patch(
        f"{API_BASE_URL}/user/name",
        json=data,
    )
    assert response.status_code == 401


def test_valid_edit_name(authenticated_user_headers, user):
    data = {
        "name": generate_unique_name()
    }
    response = requests.patch(
        f"{API_BASE_URL}/user/name",
        json=data,
        headers=authenticated_user_headers
    )
    assert response.status_code == 200
    assert response.json()["user"]["name"] != user["name"]


def test_empty_edit_name(authenticated_user_headers):
    data = {
        "name": ""
    }
    response = requests.patch(
        f"{API_BASE_URL}/user/name",
        json=data,
        headers=authenticated_user_headers
    )
    assert response.status_code == 422








import requests
import config
import pytest
from src.enums.global_enums import GlobalErrorMessages


def test_check_conn():
    data = {"email": "check_conn@check.conn"}
    url = config.SERVICE_URL + "exist/"
    response = requests.post(url=url, data=data)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE


def test_check_yavshoke_positive(registered_users):
    user = registered_users[0]
    data = {"email": user["email"]}
    url = config.SERVICE_URL + "exist/"
    response = requests.post(url=url, json=data)
    json_body = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert json_body.get("exist") is True, GlobalErrorMessages.WRONG_BODY


def test_check_yavshoke_negative():
    data = {"email": config.unregister_email}
    url = config.SERVICE_URL + "exist/"
    response = requests.post(url=url, json=data)
    json_body = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert json_body.get("exist") is False, GlobalErrorMessages.WRONG_BODY


@pytest.mark.parametrize("user_index", [0, 1, 2])
def test_check_auth_positive(registered_users, user_index):
    user = registered_users[user_index]
    url = config.SERVICE_URL + "auth/login"
    data = {
        "email": user["email"],
        "password": user["password"]
    }
    response = requests.post(url=url, json=data)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE


def test_check_auth_negative():
    url = config.SERVICE_URL + "auth/login"
    data = {
        "email": config.unregister_email,
        "password": config.unregister_pass
    }
    response = requests.post(url=url, json=data)

    assert response.status_code == 422, GlobalErrorMessages.WRONG_STATUS_CODE


def test_swap_name(registered_users):
    user = registered_users[0]
    login_url = config.SERVICE_URL + "auth/login"
    auth_data = {
        "email": user["email"],
        "password": user["password"]
    }
    login_response = requests.post(login_url, json=auth_data)
    assert login_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE

    token = login_response.json().get("token")
    assert token, GlobalErrorMessages.WRONG_TOKEN

    headers = {
        "Authorization": f"Bearer {token}"
    }
    user_info_url = config.SERVICE_URL + "user/me"
    response_before = requests.get(user_info_url, headers=headers)
    assert response_before.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    name_before = response_before.json().get("user", {}).get("name")
    print(f"Имя до: {name_before}")

    swap_name_url = config.SERVICE_URL + "user/name"
    switch_data = {
        "name": config.new_name
    }
    switch_response = requests.patch(swap_name_url, json=switch_data, headers=headers)
    assert switch_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE

    response_after = requests.get(user_info_url, headers=headers)
    assert response_after.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    name_after = response_after.json().get("user", {}).get("name")
    print(f"Имя после: {name_after}")

    assert name_after == config.new_name, (f" Имя не изменилось: ожидалось '{config.new_name}'"
                                           f", получено '{name_after}'")

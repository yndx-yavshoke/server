import requests
import pytest
from data import exist_data


@pytest.mark.exist
def test_user_exist_with_user_exist(base_url):
    url = f"{base_url}/exist"
    response = requests.post(url, json=exist_data.user_exist)
    data = response.json()

    assert data['exist'] == True, f"Пользователь с email {exist_data.user_exist['email']} должен существовать в базе данных"
@pytest.mark.exist
def test_user_exist_with_user_not_exist(base_url):
    url = f"{base_url}/exist"
    response = requests.post(url, json=exist_data.user_not_exist)
    data = response.json()

    assert data['exist'] == False, f"Пользователь с email {exist_data.user_exist['email']} не должен существовать в базе данных"
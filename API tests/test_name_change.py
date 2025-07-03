import requests
import pytest
import random
from conf import link
from Models import headers, NameChange, registration, randString

@pytest.fixture(scope="function", autouse=True)
def token():
    return registration()[0]['token']


@pytest.mark.parametrize('name', [randString(random.randint(1, 50)) for _ in range(10)])
def testNameChange(token: str, name: str):
    data = NameChange(name).json()
    head = headers(token)
    req = requests.patch(link + 'user/name', data=data, headers=head)
    assert req.status_code == 200
    assert req.json()["user"]["name"] == name
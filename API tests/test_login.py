import pytest
from conf import link
from Models import registration, Login, headers, mailGenerator, passwordGenerator
import requests

@pytest.mark.parametrize('userData', [registration() for _ in range(10)])
def testWithRealUser(userData):
    data = Login(userData[0]["user"]["email"], userData[1]).json()
    req = requests.post(link + 'auth/login', data=data, headers=headers())
    assert req.status_code == 200
    assert req.json()["user"]["email"] == userData[0]["user"]["email"]


@pytest.mark.parametrize('userData', [[mailGenerator(), passwordGenerator()] for _ in range(10)])
def testWithoutRealUser(userData):
    data = Login(userData[0], userData[1]).json()
    req = requests.post(link + 'auth/login', data=data, headers=headers())
    assert req.status_code == 422
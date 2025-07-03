import random

import requests
import pytest
from Models import registration, ShokCheck, headers, mailGenerator, randString
from conf import link


@pytest.mark.parametrize('userData', [registration() for _ in range(10)])
def testWithRealUser(userData):
    data = ShokCheck(userData[0]["user"]["email"]).json()
    req = requests.post(link + 'exist', data=data, headers=headers())
    assert req.status_code == 200
    assert req.json()["exist"] == True


@pytest.mark.parametrize('userData', [mailGenerator() for _ in range(10)])
def testWithoutRealUser(userData):
    data = ShokCheck(userData).json()
    req = requests.post(link + 'exist', data=data, headers=headers())
    assert req.status_code == 200
    assert req.json()["exist"] == False

@pytest.mark.parametrize('userData', [randString(random.randint(5, 25)) for _ in range(10)])
def testWithNotEmail(userData):
    data = ShokCheck(userData).json()
    req = requests.post(link + 'exist', data=data, headers=headers())
    assert req.status_code == 400

@pytest.mark.parametrize('json', [{}, registration()[0], {"select *": "abcdbca"}, '', "{email: mail@mai.ru}"])
def testWithBrokenJSON(json):
    req = requests.post(link + 'exist', data=json, headers=headers())
    assert req.status_code == 400
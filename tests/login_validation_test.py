import requests
from fixtures import *

fake = Faker()

def test_login_wrong_pass(register_url, login_url, random_mail, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": random_age
    })

    r = requests.post(login_url, json={
        "email": random_mail,
        "password": fake.pystr()
    })
    assert r.status_code  == 422

def test_login_user_does_not_exist(login_url, random_mail, random_pass):
    r = requests.post(login_url, json={
        "email": random_mail,
        "password": random_pass
    })
    assert r.status_code  == 422

def test_login_no_mail(login_url, random_pass):
    r = requests.post(login_url, json={
        "email": "",
        "password": random_pass
    })
    assert r.status_code  == 422

def test_login_no_password(login_url, random_mail):
    r = requests.post(login_url, json={
        "email": random_mail,
        "password": ""
    })
    assert r.status_code  == 422

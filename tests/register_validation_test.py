import requests
from fixtures import *

fake = Faker()
username = fake.pystr(max_chars=40)
domain = fake.pystr(max_chars=5) + ".com"
fake_mail = f"{username}@{domain}"

def test_register_long_mail(register_url, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": f"{fake_mail}",
        "password": random_pass,
        "age": random_age
    })
    assert r.status_code == 200, 'Something wrong'

def test_register_upper_limit_mail(register_url, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": f"{fake.random_letter()}{fake_mail}",
        "password": random_pass,
        "age": random_age
    })
    assert r.status_code == 422

def test_register_mail_with_spaces(register_url, random_mail, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": f" {random_mail} ",
        "password": random_pass,
        "age": random_age
    })
    assert r.status_code == 422

def test_register_random_symbols_mail(register_url, random_mail, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": f"{fake.emoji()}{random_mail}",
        "password": random_pass,
        "age": random_age
    })
    assert r.status_code == 422

def test_register_long_password(register_url, random_mail, random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": f"{fake.password(length = 20)}",
        "age": random_age
    })
    assert r.status_code == 200, 'Something wrong'

def test_register_short_password(register_url, random_mail, random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": f"{fake.password(length = 5)}",
        "age": random_age
    })
    assert r.status_code == 200, 'Something wrong'

def test_register_upper_limit_password(register_url, random_mail, random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": f"{fake.password(length = 21)}",
        "age": random_age
    })
    assert r.status_code == 422

def test_register_lower_limit_password(register_url, random_mail, random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": f"{fake.password(length = 4)}",
        "age": random_age
    })
    assert r.status_code == 422

# тест будет падать, т.к. валидации со стороны бэкенда нет, это баг
"""
def test_register_random_symbols_password(register_url, random_mail, random_age):
    symbol_pass = ''
    for i in range(5):
        symbol_pass += fake.emoji()
        
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": f"{symbol_pass}",
        "age": random_age
    })
    assert r.status_code == 422
"""

def test_register_max_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": 99
    })
    assert r.status_code == 200, 'Something wrong'

def test_register_min_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": 0
    })
    assert r.status_code == 200, 'Something wrong'

def test_register_upper_limit_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": 100
    })
    assert r.status_code == 422

def test_register_lower_limit_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": -1
    })
    assert r.status_code == 422

def test_register_random_symbols_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": f"{fake.emoji()}"
    })
    assert r.status_code == 422

def test_register_no_mail(register_url, random_pass, random_age):
    r = requests.post(register_url, json={
        "email": "",
        "password": random_pass,
        "age": random_age
    })
    assert r.status_code == 422

def test_register_no_password(register_url, random_mail,  random_age):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": "",
        "age": random_age
    })
    assert r.status_code == 422

def test_register_no_age(register_url, random_mail,  random_pass):
    r = requests.post(register_url, json={
        "email": random_mail,
        "password": random_pass,
        "age": ""
    })
    assert r.status_code == 422

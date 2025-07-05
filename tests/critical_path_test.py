import requests
from fixtures import *

fake = Faker()

user_mail = fake.email()
user_password = fake.password(length=randint(5, 20))
user_age = randint(0,  99)

def test_get_health(health_url):
    r = requests.get(health_url)
    assert r.status_code == 200, 'Something wrong, server is not available'

    r_body = r.json()
    assert r_body['status'] == 'ok', 'Something wrong'
    assert r_body['database'] == 'connected', 'Something wrong, DB is not available'

def test_post_no_exist(exist_url):
    r = requests.post(exist_url, data={
        "email": f"{user_mail}"
    })
    r_body = r.json()
    assert r_body['exist'] == False

def test_get_no_user(userme_url):
    header = {
        "Authorization": f"Bearer {fake.sha256()}"
    }
    r = requests.get(userme_url, headers=header)
    assert r.status_code == 401

def test_post_auth_register(register_url):
    r = requests.post(register_url, json={
        "email": f"{user_mail}",
        "password": f"{user_password}",
        "age": user_age
    })
    assert r.status_code == 200, 'Something wrong'

    r = requests.post(register_url, json={
        "email": f"{user_mail}",
        "password": f"{user_password}",
        "age": user_age
    })
    assert r.status_code == 422

def test_post_exist(exist_url):
    r = requests.post(exist_url, data={
        "email": f"{user_mail}"
    })
    r_body = r.json()
    assert r_body['exist'] == True, 'User no exist'

def test_post_login(login_url):
    r = requests.post(login_url, json={
        "email": f"{user_mail}",
        "password": f"{user_password}"
    })
    assert r.status_code  == 200, 'Wrong email or password'

def test_get_user(login_url, userme_url):
    r = requests.post(login_url, json={
        "email": f"{user_mail}",
        "password": f"{user_password}",
    })
    login_body = r.json()
    token = login_body['token']
    header = {
        'Authorization': f'Bearer {token}'
    }

    r = requests.get(userme_url, headers=header)
    r_body = r.json()
    user_body = r_body['user']
    assert r.status_code == 200, 'Something wrong'
    assert user_body['email'] == user_mail
    assert user_body['age'] == user_age

def test_patch_user(login_url, username_url):
    r = requests.post(login_url, json={
        "email": f"{user_mail}",
        "password": f"{user_password}",
    })
    login_body = r.json()
    token = login_body['token']
    header = {
        'Authorization': f'Bearer {token}'
    }

    r = requests.patch(username_url, headers=header, json={
        "name": f"{fake.name()}"
    })
    assert r.status_code == 200, 'Something wrong'

def test_patch_no_user(username_url):
    header = {
        "Authorization": f"Bearer {fake.sha256()}"
    }
    r = requests.patch(username_url, headers=header, json={
        "name": f"{fake.name()}"
    })
    assert r.status_code == 401

import requests

def test_vshok():
    url = "https://api.yavshok.ru/exist"
    payload = {
        "email": "qwerty@yandex.ru"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

class Test_login_users:
    def test_login_young_user200(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qwerty@yandex.ru",
            "password": "123456"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 200
        print(response.json())

    def test_login_young_user422(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qwerty@ya.ru",
            "password": "123456"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 422
        print(response.json())

    def test_login_young_user500(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qwerty@ya.ru",
            "password": "123456"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 500
        print(response.json())

    def test_login_adult_user200(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "asdfg@ya.ru",
            "password": "654321"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 200
        print(response.json())

    def test_login_adult_user422(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "asdfg@ya.ru",
            "password": "65321"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 422
        print(response.json())

    def test_login_adult_user500(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "asdfg@ya.ru",
            "password": "654321"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 500
        print(response.json())

    def test_login_old_user200(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qw@qw.qw",
            "password": "qwqwqw"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 200
        print(response.json())

    def test_login_old_user422(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qw@qw.qw",
            "password": "qwqww"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 422
        print(response.json())

    def test_login_old_user500(self):
        url="https://api.yavshok.ru/auth/login"
        payload = {
            "email": "qw@qw.qw",
            "password": "qwqwqw"
        }
        response = requests.post(url, json = payload)
        assert response.status_code == 500
        print(response.json())

class Test_name_substitution:
    def test_user_name200(self):
        auth = requests.post(
            "https://api.yavshok.ru/auth/login",
            json={"email": "qwerty@yandex.ru", "password": "123456"})
        token = auth.json()["token"]
        response = requests.patch(
            "https://api.yavshok.ru/user/name",
            json={"name": "NewName"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        print(response.json())

    def test_user_name401(self):
        auth = requests.post(
            "https://api.yavshok.ru/auth/login",
            json={"email": "qwerty@yandex.ru", "password": "123456"})
        token = "token"
        response = requests.patch(
            "https://api.yavshok.ru/user/name",
            json={"name": "NewName"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 401
        print(response.json())

    def test_user_name422(self):
        auth = requests.post(
            "https://api.yavshok.ru/auth/login",
            json={"email": "qwerty@yandex.ru", "password": "123456"})
        token = auth.json()["token"]
        response = requests.patch(
            "https://api.yavshok.ru/user/name",
            json={"email": "NewName"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 422
        print(response.json())
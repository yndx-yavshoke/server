import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, email, password):
        url = f"{self.base_url}/auth/login"
        resp = requests.post(url, json={"email": email, "password": password})
        resp.raise_for_status()
        return resp.json()["token"]

    def get_profile(self, token):
        url = f"{self.base_url}/user/me"
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp

    def update_name(self, token, new_name):
        url = f"{self.base_url}/user/name"
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.patch(url, json={"name": new_name}, headers=headers)
        resp.raise_for_status()
        return resp

    def check_user_exists(self, email):
        url = f"{self.base_url}/exist"
        resp = requests.post(url, json={"email": email})
        resp.raise_for_status()
        return resp

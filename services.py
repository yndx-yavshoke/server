from api_client import APIClient

class UserService:
    def __init__(self, client: APIClient):
        self.client = client

    def login_and_get_profile(self, email, password):
        token = self.client.login(email, password)
        profile_resp = self.client.get_profile(token)
        return profile_resp.json()

    def login_and_change_name(self, email, password, new_name):
        token = self.client.login(email, password)
        self.client.update_name(token, new_name)
        profile_resp = self.client.get_profile(token)
        return profile_resp.json()

class ShokService:
    def __init__(self, client: APIClient):
        self.client = client

    def check_shok_status(self, email):
        resp = self.client.check_user_exists(email)
        data = resp.json()
        if data["exist"]:
            return {"message": "Ты уже в ШОКе"}
        else:
            return {"message": "Ты ещё не в ШОКе"}
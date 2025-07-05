from ..api_client import ApiClient

class AuthEndpoint:
    def __init__(self, client: ApiClient):
        self._client = client

    def login(self, email: str, password: str) -> dict[str, object]:
        data = {"email": email, "password": password}
        return self._client._make_request('POST', '/auth/login', json=data)

    def register(self, email: str, password: str, age: int) -> dict[str, object]:
        data = {"email": email, "password": password, "age": age}
        return self._client._make_request('POST', '/auth/register', json=data)
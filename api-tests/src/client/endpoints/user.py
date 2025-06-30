from ..api_client import ApiClient
from .auth import AuthEndpoint

class UserEndpoint:
    def __init__(self, client: ApiClient):
        self._client = client
        self._auth = AuthEndpoint(client)

    def change_name(self, new_name: str, email: str, password: str) -> dict[str, object]:
        auth_response = self._auth.login(email, password)
        
        token = auth_response['body']['token'] # type: ignore
        
        if not token:
            raise Exception("Failed to get authentication token")
        
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {"name": new_name}
        return self._client._make_request('PATCH', '/user/name', json=data, headers=headers)

    def get_current_user(self, email: str, password: str) -> dict[str, object]:
        auth_response = self._auth.login(email, password)
        
        token = auth_response['body']['token'] # type: ignore
        
        if not token:
            raise Exception("Failed to get authentication token")
        
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        return self._client._make_request('GET', '/user/me', headers=headers)
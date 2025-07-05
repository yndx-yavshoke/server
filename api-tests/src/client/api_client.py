import requests

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token: str | None = None
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> dict[str, object]:
        url = f"{self.base_url}{endpoint}"
        
        if self.token:
            headers = kwargs.get('headers', {})
            headers['Authorization'] = f"Bearer {self.token}"
            kwargs['headers'] = headers
        
        response = requests.request(method, url, **kwargs)
        try:
            body = response.json()
        except Exception:
            body = response.text
        return {
            "status_code": response.status_code,
            "body": body
        }

    def check_health(self) -> dict[str, object]:
        return self._make_request('GET', '/health')

    def check_exist(self, email: str) -> dict[str, object]:
        data = {"email": email}
        return self._make_request('POST', '/exist', json=data)
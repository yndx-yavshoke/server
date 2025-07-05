import requests
from fixtures import username_url

def test_user_no_name(username_url):
    r = requests.patch(username_url, json={
        "name": ""
    })
    assert r.status_code == 422

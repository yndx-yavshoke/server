import requests
import random
from functions import generate_valid_email,generate_valid_password,generate_new_name,url


def test_change_name():
    register_url = url + "/auth/register"
    email = generate_valid_email()
    password = generate_valid_password()
    age = random.randint(0, 99) 
    
    register_payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    register_response = requests.post(register_url, json=register_payload)
    

    assert register_response.status_code in (200, 201), \
        f"Registration failed: {register_response.text}"
    
    data = register_response.json()

    token = data["token"]
    name_changed_url = url+"/user/name"

    changed_payload = {
        "name": f"{generate_new_name()}"
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    change_name_response = requests.patch(name_changed_url, json=changed_payload, headers=headers)
    assert change_name_response.status_code == 200, \
        f"Name change failed: {change_name_response.text}"

def test_change_name_without_token():
    register_url = url + "/auth/register"
    email = generate_valid_email()
    password = generate_valid_password()
    age = random.randint(0, 99) 
    
    register_payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    register_response = requests.post(register_url, json=register_payload)
    

    assert register_response.status_code in (200, 201), \
        f"Registration failed: {register_response.text}"
    
    name_changed_url = url+"/user/name"

    changed_payload = {
        "name": f"{generate_new_name()}"
    }

    change_name_response = requests.patch(name_changed_url, json=changed_payload)
    assert change_name_response.status_code == 401

def test_change_name_invalid():
    register_url = url + "/auth/register"
    email = generate_valid_email()
    password = generate_valid_password()
    age = random.randint(0, 99) 
    
    register_payload = {
        "email": email,
        "password": password,
        "age": age
    }
    
    register_response = requests.post(register_url, json=register_payload)
    

    assert register_response.status_code in (200, 201), \
        f"Registration failed: {register_response.text}"
    
    data = register_response.json()

    token = data["token"]
    name_changed_url = url+"/user/name"

    changed_payload = {
        "name": ""
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    change_name_response_empty_name = requests.patch(name_changed_url, json=changed_payload, headers=headers)
    assert change_name_response_empty_name.status_code == 422
    

    changed_payload_invalid = {
        "name": "Admin🚀"
    }
    change_name_response_invalid_name = requests.patch(name_changed_url,json=changed_payload_invalid,headers=headers)

    assert change_name_response_invalid_name.status_code == 422

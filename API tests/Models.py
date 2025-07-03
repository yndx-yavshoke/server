import dataclasses
from dataclasses import dataclass
import json
import random
import string
import requests
from conf import link




@dataclass
class ShokCheck:
    email: str

    def json(self):
        return json.dumps(dataclasses.asdict(self))

@dataclass
class Login:
    email: str
    password: str

    def json(self):
        return json.dumps(dataclasses.asdict(self))

@dataclass
class Registration:
    email: str
    password: str
    age: int

    def json(self):
        return json.dumps(dataclasses.asdict(self))

@dataclass
class NameChange:
    name: str

    def json(self):
        return json.dumps(dataclasses.asdict(self))

def headers(token=None):
    if token:
        return { 'Authorization': f'Bearer {token}', 'Content-Type': 'application/json' }
    return {'Content-Type': 'application/json'}

def registration():
    email = f'{''.join([random.choice(string.ascii_letters) for _ in
                        range(10)])}@ya.ru'
    password = ''.join([random.choice(string.ascii_letters) for _ in
                        range(10)])
    age = random.randint(0, 100)
    data = Registration(email, password, age).json()
    reg_response = requests.post(link + 'auth/register', data=data, headers=headers())
    return reg_response.json(), password


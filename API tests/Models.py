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

def randString(size: int):
    return ''.join([random.choice(string.ascii_letters) for _ in
                        range(size)])
def mailGenerator():
    return f'{randString(random.randint(3,25))}@{randString(random.randint(2,6))}.{randString(random.randint(2,3))}'

def passwordGenerator():
    return randString(random.randint(6,20))


def registration():
    email = mailGenerator()
    password = passwordGenerator()
    age = random.randint(0, 100)
    data = Registration(email, password, age).json()
    reg_response = requests.post(link + 'auth/register', data=data, headers=headers())
    return reg_response.json(), password


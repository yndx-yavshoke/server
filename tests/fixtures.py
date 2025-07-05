import os
import pytest
from dotenv import load_dotenv
from faker import Faker
from random import randint

fake = Faker()

load_dotenv('.env.tests')

@pytest.fixture
def health_url():
    return os.getenv('HEALTH_URL')

@pytest.fixture
def exist_url():
    return os.getenv('EXIST_URL')

@pytest.fixture
def userme_url():
    return os.getenv('USERME_URL')

@pytest.fixture
def register_url():
    return os.getenv('REGISTER_URL')

@pytest.fixture
def login_url():
    return os.getenv('LOGIN_URL')

@pytest.fixture
def username_url():
    return os.getenv('USERNAME_URL')

@pytest.fixture
def random_mail():
    return fake.email()

@pytest.fixture
def random_pass():
    return fake.password(length=randint(5, 20))

@pytest.fixture
def random_age():
    return randint(0,99)

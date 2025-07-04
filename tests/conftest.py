import pytest
import os

BASE_URL = 'http://localhost:3000'

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
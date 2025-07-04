import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR.parent, '.env'))

API_PORT = os.getenv('DEBUG', '3000')

USE_DOCKER_NETWORK = False
if USE_DOCKER_NETWORK:
    API_BASE_URL = f'http://server:{API_PORT}'
else:
    API_BASE_URL = f'http://localhost:{API_PORT}'

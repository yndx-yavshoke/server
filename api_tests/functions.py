import secrets
import string



def generate_valid_email():
    alphabet = string.ascii_letters + string.digits
    local_part = ''.join(secrets.choice(alphabet) for _ in range(38))
    return f"{local_part}@example.com"

def generate_valid_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(19))

def generate_new_name():
    alphabet = string.ascii_letters + string.digits
    name = ''.join(secrets.choice(alphabet) for _ in range(20))
    return f"{name}"

url = "http://localhost:3000"
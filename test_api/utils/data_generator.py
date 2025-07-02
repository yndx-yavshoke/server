import random
import string

# Генерирует валидный payload для регистрации пользователя
# email, password (8 символов), age (0-99)
def generate_valid_user_payload():
    payload = {
        "email": f"user{random.randint(100000, 999999)}@example.com",
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=8)),  # всегда 8 символов
        "age": random.randint(0, 99)  # например, только взрослые
    }
    return payload

# Генерирует невалидный payload для регистрации (неправильный email, короткий пароль, некорректный age)
def generate_invalid_user_payload():
    payload = {
        "email": "invalid-email",  # Некорректный формат
        "password": "123",  # Меньше 5 символов
        "age": 100  # За пределами 0-99
    }
    return payload

# Генерирует payload для обновления имени пользователя (от 1 до 50 символов)
def generate_name_update_payload():
    payload = {
        "name": ''.join(random.choices(string.ascii_letters, k=random.randint(1, 50)))
    }
    return payload

# Генерирует уникальный идентификатор пользователя (20 цифр)
def generate_user_id():
    return str(random.randint(10000000000000000000, 99999999999999999999))

# Генерирует тестовый email для регистрации
def generate_test_email():
    return f"test{generate_user_id()[:8]}@example.com"
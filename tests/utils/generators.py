import random
import string

# Файл utils.py предназначен для генерации входных данных
# В качестве входных данных предоставляется body post-запросов,
# а также любая другая полезная информация (имя + ID-пользователя в связке с почтой)



# Функция создает body post-запроса
# Возврат payload'a содержит правильный e-mail, pass, age
# В соответствии с требованиями
def generate_valid_user_payload():
    payload = {
        "email": f"Vi{random.randint(100000, 999999)}Test@removespread.ru",
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)), 
        "age": random.randint(0, 99)
    }
    return payload


# Функция создает body post-запроса
# Возврат payload;a содержит некорректный формат email, короткий пароль и выходящий за рамки возраст
def generate_invalid_payload():
    payload = {
        "email": "incorrect-email",
        "password": "11",
        "age": 122
    }
    return payload

def generate_name_update_payload():
    payload = {
        "name": ''.join(random.choices(string.ascii_letters, k=random.randint(1, 50)))
    }
    return payload

def generate_user_id():
    return str(random.randint(10000000000000000000, 99999999999999999999))

def generate_test_email():
    return f"Vi{generate_user_id()[:8]}@removespread.ru"
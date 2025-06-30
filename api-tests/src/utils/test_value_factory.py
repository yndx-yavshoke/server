from utils.test_data_generators import (
    generate_email, generate_password, generate_age, generate_symbol, generate_name
)

def email_5_chars():
    return f"{generate_symbol()}@{generate_symbol()}.r"

def email_4_chars():
    return f"{generate_symbol()}@{generate_symbol()}."

def email_50_chars():
    return generate_symbol() * 38 + "@example.com"

def email_51_chars():
    return generate_symbol() * 39 + "@example.com"

def long_name():
    return generate_symbol() * 45

def too_long_name():
    return generate_symbol() * 256

def random_russian_name():
    return generate_name(language="ru_RU")

value_factory = {
    "random_email": generate_email,
    "random_password": generate_password,
    "random_age": generate_age,
    "random_name": generate_name,
    "random_russian_name": random_russian_name,
    "long_name": long_name,
    "too_long_name": too_long_name,
    "email_5_chars": email_5_chars,
    "email_4_chars": email_4_chars,
    "email_with_spaces": lambda: f" {generate_email()} ",
    "email_special_char": lambda: "test@example#com",
    "email_50_chars": email_50_chars,
    "email_51_chars": email_51_chars,
    "password_4_chars": lambda: generate_password(4),
    "password_5_chars": lambda: generate_password(5),
    "password_20_chars": lambda: generate_password(20),
    "password_21_chars": lambda: generate_password(21),
    "sql_injection_email": lambda: "'; DROP TABLE users; --",
    "sql_injection_password": lambda: "'; DROP TABLE users; --",
    "age_0": lambda: 0,
    "age_99": lambda: 99,
    "age_100": lambda: 100,
    "age_negative": lambda: -1,
    "age_letters": lambda: "abc",
    "null_email": lambda: None,
    "null_password": lambda: None,
    "null_age": lambda: None,
    "": lambda: "",
}

def get_test_value(key, **kwargs):
    if key == "existing_email" or key == "api_username":
        return kwargs.get("api_username")
    if key == "api_password":
        return kwargs.get("api_password")
    if key == "api_username_trim":
        return f" {kwargs.get('api_username')} "
    if key == "not_register":
        return generate_email()
    if key == "any_password" or key == "wrong_password":
        return generate_password()
    if key in value_factory:
        return value_factory[key]()
    return key 
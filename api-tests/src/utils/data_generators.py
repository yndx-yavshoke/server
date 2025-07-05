from faker import Faker

fake = Faker()

def generate_email() -> str:
    return fake.email()

def generate_fixed_email(length: int) -> str:
    if length < 5:
        length = 5
    if length < 13:
        return f"{generate_symbol()}*{(length - 4)}@{generate_symbol()}.r"
    return generate_string((length - 12)) + "@example.com"

def generate_string(length: int) -> str:
    result: list = []
    for i in range(length):
        result.append(generate_symbol())
    return ''.join(result)

def generate_password(length: int | None = None) -> str:
    if length is None:
        return fake.password()
    return fake.password(length)

def generate_name(language: str | None = None) -> str:
    if language:
        localized_fake = Faker(language)
        return localized_fake.name()
    else:
        return fake.user_name()

def generate_age() -> int:
    return fake.random_int(min=0, max=99)

def generate_symbol() -> str:
    return 'abcdefghijklmnopqrstuvwxyz'[fake.random_int(min=0, max=25)]

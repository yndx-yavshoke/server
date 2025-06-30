from faker import Faker

fake = Faker()

def generate_email():
    return fake.email()

def generate_password(length=None):
    if length is None:
        return fake.password()
    return fake.password(length)

def generate_name(language=None):
    if language:
        localized_fake = Faker(language)
        return localized_fake.name()
    else:
        return fake.user_name()

def generate_age():
    return fake.random_int(min=0, max=99)

def generate_symbol():
    return 'abcdefghijklmnopqrstuvwxyz'[fake.random_int(min=0, max=25)]

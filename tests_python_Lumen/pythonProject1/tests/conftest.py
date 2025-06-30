import pytest
from src.utils.register_user import register_user
import config


@pytest.fixture(scope="session", autouse=True)
def registered_users():
    """
    Фикстура по регистрации пользователей
    Передаем почты пароли и возраст из файла config
    Дальше вызывает функцию регистрации из src/utils/register_user.py
    """

    users = [
        {"email": config.register_email_1, "password": config.register_pass_1, "age": 18},
        {"email": config.register_email_2, "password": config.register_pass_2, "age": 30},
        {"email": config.register_email_3, "password": config.register_pass_3, "age": 70},
    ]

    for user in users:
        register_user(user["email"], user["password"], user["age"])

    return users

class Exist:
# почта зарегистрированного пользователя
    exist = {
        "email": "ev@example.com"
    }
# почта незарегистрированного пользователя
    notexist = {
        "email": "no_such_user@example.com"
    }

class Login:
# пустые поля
    empty = {
        "email": "",
        "password": ""
    }
# только почта
    only_email = {
        "email": "ev@example.com",
        "password": ""
    }
# только пароль
    only_password = {
        "email": "",
        "password": "string"
    }
# почта и пароль зарегистрированного
    register = {
        "email": "ev@example.com",
        "password": "string"
    }
# неверный пароль
    wrong_password = {
        "email": "ev@example.com",
        "password": "string1"
    }
# почта незарегистрированного
    not_register = {
        "email": "no_such_user@example.com",
        "password": "string"

    }

class NewName:
# пустые поля
    empty = ''
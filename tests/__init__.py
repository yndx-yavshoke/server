from utils.api import YavsAPI
from utils.checking import Checking

# 1. Проверка на "шоковость"
def test_shock():
    response = YavsAPI.shock()
    Checking.check_status_code(response, 200)
    assert 'exist' in response.json(), 'Нет поля exist в ответе!'
    print('Проверка на шоковость прошла успешно!')

# 2. Логин пользователя

def test_login():
    email = "blupi.job@mail.ru"
    password = "12345"
    response = YavsAPI.login(email, password)
    Checking.check_status_code(response, 200)
    data = response.json()
    assert 'token' in data, 'Нет токена в ответе!'
    print('Логин успешен!')
    return data['token']

# 3. Изменение имени пользователя

def test_change_name():
    token = test_login()  # Получаем токен через логин
    new_name = "ТестовоеИмя"
    response = YavsAPI.change_name(token, new_name)
    Checking.check_status_code(response, 200)
    data = response.json()
    assert data['user']['name'] == new_name, 'Имя пользователя не изменилось!'
    print('Имя пользователя успешно изменено!')

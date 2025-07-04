from utils.api import YavsAPI
from utils.checking import Checking

class TestYavsUser():
    def test_full_user_flow(self):
        print('\nПРОВЕРКА НА "ШОКОВОСТЬ" (POST /exist)')
        response_shock = YavsAPI.shock()
        Checking.check_status_code(response_shock, 200)
        Checking.check_json_token(response_shock, ['exist'])
        assert response_shock.json().get('exist') is True, 'пользователь не найден (exist != True)'
        print('проверка на шоковость прошла успешно!')

        print('\nЛОГИН ПОЛЬЗОВАТЕЛЯ (POST /auth/login)')
        email = "blupi.job@mail.ru"
        password = "123456"
        response_login = YavsAPI.login(email, password)
        Checking.check_status_code(response_login, 200)
        Checking.check_json_token(response_login, ['token', 'user'])
        token = response_login.json().get('token')
        assert token, 'токен не получен!'
        print('логин успешен!')

        print('\nИЗМЕНЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ (PATCH /user/name)')
        response_change = YavsAPI.change_name(token)
        Checking.check_status_code(response_change, 200)
        Checking.check_json_token(response_change, ['user'])
        user = response_change.json().get('user', {})
        print('имя пользователя успешно изменено!')

        print('\nВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!')
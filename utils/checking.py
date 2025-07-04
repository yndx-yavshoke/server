import json

class Checking(object):

    @staticmethod
    def check_status_code(response, status_code):
        assert response.status_code == status_code

        if response.status_code == status_code:
            print(f'кайф! статус код: {str(response.status_code)}')
        else:
            print(f'ошибочка! статус код: {str(response.status_code)}')


    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('все поля присутствуют')

    
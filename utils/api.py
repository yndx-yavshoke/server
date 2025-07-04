from utils.http_methods import HttpMethods

base_url = 'https://api.yavshok.ru'

class YavsAPI():

    @staticmethod
    def shock():

        json_for_shock = {
        "email": "blupi.job@mail.ru"
        }

        post_resource = '/exist'
        post_url = base_url + post_resource

        print(post_url)
        response = HttpMethods.post(post_url, json_for_shock)

        print(response.json())
        print(response.status_code)
        return response

    @staticmethod
    def login(email, password):
        login_data = {
            "email": email,
            "password": password
        }
        post_resource = '/auth/login'
        post_url = base_url + post_resource
        print(post_url)
        response = HttpMethods.post(post_url, login_data)
        print(response.json())
        print(response.status_code)
        return response

    @staticmethod
    def change_name(token):
        import random
        import string
        new_name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 8)))
        new_age = random.randint(18, 99)
        patch_data = {
            "name": new_name,
            "age": new_age
        }
        patch_resource = '/user/name'
        patch_url = base_url + patch_resource
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        import requests
        response = requests.patch(patch_url, json=patch_data, headers=headers)
        print(f"изменено имя на: {new_name}, возраст на: {new_age}")
        print(response.json())
        print(response.status_code)
        return response

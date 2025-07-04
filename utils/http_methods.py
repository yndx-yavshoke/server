

import requests

class HttpMethods(object):
    headers = {'Content-Type': 'application/json'}\

    @classmethod
    def post(cls,url,data):
        response = requests.post(url, json = data, headers = cls.headers)
        return response

    @classmethod
    def patch(cls,url,data):
        response = requests.patch(url, json = data, headers = cls.headers)
        return response
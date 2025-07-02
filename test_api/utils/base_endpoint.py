import logging
from utils.retry import retry


class BaseEndpoint:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
        self.response = None
        self.response_json = None
        # Устанавливаем заголовок по умолчанию для всех запросов
        self.session.headers.update({"Content-Type": "application/json"})  # Устанавливаем по умолчанию

    def _log_request(self, method, url, **kwargs):
        # Логируем отправляемый запрос
        payload = kwargs.get('json') or kwargs.get('params')
        logging.info(f"[REQUEST] {method} {url} | payload/params: {payload}")

    def _log_response(self, response):
        # Логируем полученный ответ
        try:
            content = response.json()
        except Exception:
            content = response.text
        logging.info(f"[RESPONSE] {response.status_code} | content: {content}")

    @retry(max_attempts=10, delay=1.0)
    def post(self, path: str, payload=None, expected_status=200, **kwargs):
        # POST-запрос к API
        url = f"{self.base_url}{path}"
        self._log_request("POST", url, json=payload)
        try:
            self.response = self.session.post(url, json=payload, **kwargs)
            self._log_response(self.response)
        except Exception as e:
            logging.error(f"Ошибка при POST-запросе: {e}")
            raise
        self._handle_response(expected_status)
        return self.response

    @retry(max_attempts=10, delay=1.0)
    def get(self, path: str, params=None, expected_status=200, **kwargs):
        # GET-запрос к API
        url = f"{self.base_url}{path}"
        self._log_request("GET", url, params=params)
        try:
            self.response = self.session.get(url, params=params, **kwargs)
            self._log_response(self.response)
        except Exception as e:
            logging.error(f"Ошибка при GET-запросе: {e}")
            raise
        self._handle_response(expected_status)
        return self.response

    @retry(max_attempts=10, delay=1.0)
    def put(self, path: str, payload=None, expected_status=200, **kwargs):
        # PUT-запрос к API
        url = f"{self.base_url}{path}"
        self._log_request("PUT", url, json=payload)
        try:
            self.response = self.session.put(url, json=payload, **kwargs)
            self._log_response(self.response)
        except Exception as e:
            logging.error(f"Ошибка при PUT-запросе: {e}")
            raise
        self._handle_response(expected_status)
        return self.response

    @retry(max_attempts=10, delay=1.0)
    def patch(self, path: str, payload=None, expected_status=200, **kwargs):
        # PATCH-запрос к API
        url = f"{self.base_url}{path}"
        self._log_request("PATCH", url, json=payload)
        try:
            self.response = self.session.patch(url, json=payload, **kwargs)
            self._log_response(self.response)
        except Exception as e:
            logging.error(f"Ошибка при PATCH-запросе: {e}")
            raise
        self._handle_response(expected_status)
        return self.response

    @retry(max_attempts=10, delay=1.0)
    def delete(self, path: str, expected_status=200, **kwargs):
        # DELETE-запрос к API
        url = f"{self.base_url}{path}"
        self._log_request("DELETE", url)
        try:
            self.response = self.session.delete(url, **kwargs)
            self._log_response(self.response)
        except Exception as e:
            logging.error(f"Ошибка при DELETE-запросе: {e}")
            raise
        self._handle_response(expected_status)
        return self.response

    def set_token(self, token):
        # Устанавливаем токен авторизации для сессии
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def check_field_value(self, field, expected_value):
        # Проверка значения поля в ответе
        assert self.response_json.get(field) == expected_value, (
            f"Expected {field} to be {expected_value}, got {self.response_json.get(field)}")

    def check_response_content(self, expected_code=None, required_fields=None, message_contains=None):
        # Проверка содержимого ответа по коду, наличию полей и тексту сообщения
        if expected_code is not None and "code" in self.response_json:
            assert self.response_json["code"] == expected_code, (
                f"Expected code {expected_code}, got {self.response_json['code']}"
            )
        if required_fields:
            for field in required_fields:
                assert field in self.response_json, f"Response should contain '{field}' field"
        if message_contains and "message" in self.response_json:
            for text in message_contains:
                assert text in self.response_json["message"], (
                    f"Response message should contain '{text}'"
                )

    def _handle_response(self, expected_status):
        # Проверка статуса ответа и парсинг JSON
        if self.response is not None:
            logging.debug(f"Проверка статуса ответа: {self.response.status_code} (ожидался {expected_status})")
        assert self.response.status_code == expected_status, (
            f"Expected status {expected_status}, got {self.response.status_code}"
        )
        try:
            self.response_json = self.response.json()
        except ValueError as e:
            logging.error(f"Ошибка при парсинге JSON: {e}")
            self.response_json = None
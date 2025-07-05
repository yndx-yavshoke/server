# Yavshok API Tests

Automated tests for [Yavshok REST API](https://api.yavshok.ru/swagger)

## Установка

### 1. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

```bash
cp .env.example .env
```

### 2. Для запуска тестов:

```bash
pytest api-tests/src/tests/
 ```

### 3. Для запуска тестов с выводом дополнительной информации:

```bash
pytest api-tests/src/tests/ -v -s
```
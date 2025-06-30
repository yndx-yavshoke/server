# 🚀 Elysia Server

## 🔧 Требования

Перед началом работы убедитесь, что у вас установлены:

- **Docker** (версия 20.0 или выше)
- **Docker Compose** (версия 2.0 или выше)
- **Git** (для клонирования репозитория)

### Проверка установки Docker

```bash
docker --version
docker-compose --version
```

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/yndx-yavshoke/server
cd server
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

```bash
cp .env.example .env  # если есть .env.example
# или создайте .env файл вручную
```

### 3. Запуск сервиса

**Для Unix/Linux/macOS:**
```bash
chmod +x run-unix.sh
./run-unix.sh
```

**Для Windows (PowerShell):**
```powershell
.\run-windows.ps1
```

### 4. Проверка работы

После запуска сервис будет доступен по адресу:
- **Основное API:** http://localhost:3000
- **Swagger документация:** http://localhost:3000/swagger

## 🏃‍♂️ Запуск сервиса

### Автоматический запуск (рекомендуется)

Проект включает готовые скрипты для запуска:

**Unix/Linux/macOS:**
```bash
./run-unix.sh up        # Запуск сервисов (по умолчанию)
./run-unix.sh down      # Остановка сервисов
./run-unix.sh logs      # Просмотр логов
./run-unix.sh build     # Пересборка образов
./run-unix.sh restart   # Перезапуск сервисов
./run-unix.sh ps        # Список запущенных сервисов
./run-unix.sh clean     # Полная очистка (контейнеры, сети, тома)
```

**Windows PowerShell:**
```powershell
.\run-windows.ps1 -Help # Справка по опциям
```

### Ручной запуск через Docker Compose

```bash
# Запуск в фоновом режиме
docker-compose up -d

# Запуск с пересборкой образов
docker-compose up -d --build

# Просмотр логов
docker-compose logs -f

# Остановка сервисов
docker-compose down
```
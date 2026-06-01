# 🤖 MyTONProvider Bot

[![TON](https://img.shields.io/badge/TON-grey?logo=TON\&logoColor=40AEF0)](https://ton.org)
[![Telegram Bot](https://img.shields.io/badge/Bot-grey?logo=telegram)](https://core.telegram.org/bots)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License](https://img.shields.io/github/license/nessshon/mytonprovider-bot)](https://github.com/nessshon/mytonprovider-bot/blob/master/LICENSE)
[![Redis](https://img.shields.io/badge/Redis-Yes?logo=redis\&color=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker\&logoColor=white)](https://www.docker.com/)

**[English version](README.md)**

Telegram-бот для мониторинга **TON Storage провайдеров** в сети TON с поддержкой телеметрии, уведомлений и аналитики.

## Описание

Проект представляет собой систему мониторинга, которая собирает данные о провайдерах
с [mytonprovider.org](https://mytonprovider.org), сохраняет их в базе данных и предоставляет пользователям удобный
интерфейс в Telegram для просмотра, подписки и получения уведомлений.

## Возможности

* Просмотр списка всех провайдеров
* Поиск по публичному ключу
* Подписка на провайдеров и управление подписками
* Включение и отключение уведомлений
* Настройка типов уведомлений (CPU, RAM, диск, перезапуск сервисов и др.)
* Многоязычный интерфейс (RU, EN, ZH-TW)
* Автоматический мониторинг финансовых показателей
* Формирование отчетов по трафику и заработку

## Установка и запуск

### Требования

* Python 3.10+
* Redis
* Docker (опционально)

### Настройка окружения

1. Скопируйте `.env.example` в `.env`:

   ```bash
   cp .env.example .env
   ```

2. Отредактируйте `.env` и заполните необходимые переменные окружения:

| Переменная              | Описание                                 | Пример значения                               |
|-------------------------|------------------------------------------|-----------------------------------------------|
| `BOT_TOKEN`             | Токен Telegram-бота от @BotFather        | `1234567890:AAE...`                           |
| `TONCENTER_API_KEY`     | Ключ доступа к TONCenter API             | `abcd1234efgh5678...`                         |
| `MYTONPROVIDER_API_KEY` | Ключ доступа к MyTONProvider API         | `abcd1234efgh5678...`                         |
| `DB_URL`                | Строка подключения к базе данных         | `sqlite+aiosqlite:///./data/database.sqlite3` |
| `REDIS_URL`             | Адрес Redis для хранения состояния       | `redis://localhost:6379/0`                    |

### Запуск

#### Локально

```bash
# Установка зависимостей
pip install -r requirements.txt

# Применение миграций базы данных
alembic upgrade head

# Запуск бота
python -m app
```

#### Через Docker

```bash
# Запуск в фоне
docker-compose up -d

# Просмотр логов
docker-compose logs -f
```

## Разработка

### Структура проекта

```
    .
    ├── app/                                # Основное приложение
    │   ├── alert/                          # Система оповещений
    │   ├── api/                            # Внешние API
    │   │   ├── mytonprovider/              # Обёртка для MyTONProvider API
    │   │   └── toncenter/                  # Обёртка для TONCenter API
    │   ├── bot/                            # Telegram-бот
    │   │   ├── dialogs/                    # Диалоги и состояния
    │   │   ├── handlers/                   # Обработчики событий
    │   │   ├── middlewares/                # Middleware
    │   │   ├── utils/                      # Утилиты
    │   │   └── commands.py                 # Команды бота
    │   ├── database/                       # База данных
    │   │   ├── models/                     # SQLAlchemy-модели
    │   │   ├── repository.py               # Репозиторий
    │   │   └── unitofwork.py               # Паттерн Unit of Work
    │   └── scheduler/                      # Планировщик задач
    │       └── jobs/                       # Фоновые задачи
    │           ├── sync_providers/         # Задачи синхронизации провайдеров
    │           ├── alerts_dispatch.py      # Обработка и рассылка оповещений
    │           ├── monthly_reports.py      # Генерация ежемесячных отчётов
    │           └── update_wallets.py       # Обновление данных кошельков провайдеров
    ├── alembic/                            # Миграции базы данных
    ├── locales/                            # Файлы локализации
    ├── data/                               # Файлы базы и сервисные данные
    └── docker-compose.yml                  # Конфигурация Docker
```

### Интеграции

* **MyTONProvider API** — данные о провайдерах и телеметрия
* **TONCenter API** — транзакции, балансы и доходность провайдеров

### Модели данных

* **ProviderModel** — информация о провайдере
* **ProviderHistoryModel** — история провайдеров (архивные данные)
* **TelemetryModel** — текущая телеметрия и метрики
* **TelemetryHistoryModel** — история телеметрии (срезы по времени)
* **WalletModel** — состояние кошелька провайдера
* **WalletHistoryModel** — история кошелька (балансы, доходы)
* **UserModel** — данные пользователя
* **UserSubscriptionModel** — подписки пользователей
* **UserAlertSettingModel** — индивидуальные настройки оповещений
* **UserTriggeredAlertModel** — журнал сработавших оповещений

### Планировщик задач

* **sync_providers/update_providers** — синхронизация и обновление провайдеров
* **sync_providers/update_telemetry** — сбор и сохранение телеметрии
* **update_wallets** — обновление данных кошельков и транзакций
* **alerts_dispatch** — обработка и рассылка оповещений
* **monthly_reports** — генерация ежемесячных отчётов

## Лицензия

Проект распространяется под лицензией [Apache-2.0](LICENSE).

# 🤖 MyTONProvider Bot

[![TON](https://img.shields.io/badge/TON-grey?logo=TON\&logoColor=40AEF0)](https://ton.org)
[![Telegram Bot](https://img.shields.io/badge/Bot-grey?logo=telegram)](https://core.telegram.org/bots)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License](https://img.shields.io/github/license/nessshon/mytonprovider-bot)](https://github.com/nessshon/mytonprovider-bot/blob/master/LICENSE)
[![Redis](https://img.shields.io/badge/Redis-Yes?logo=redis\&color=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker\&logoColor=white)](https://www.docker.com/)

**[Русская версия](README.ru.md)**

Telegram bot for monitoring **TON Storage providers** in the TON network with telemetry, alerts, and analytics support.

## Description

This project is a monitoring system that collects data about providers
from [mytonprovider.org](https://mytonprovider.org), stores it in a database, and provides users with a convenient
Telegram interface for browsing, subscribing, and receiving alerts.

## Features

* View a list of all providers
* Search by public key
* Subscribe to providers and manage subscriptions
* Enable and disable alerts
* Configure alert types (CPU, RAM, disk, service restarts, etc.)
* Multilingual interface (RU, EN, ZH-TW)
* Automatic monitoring of financial metrics
* Traffic and revenue reporting

## Installation and Run

### Requirements

* Python 3.10+
* Redis
* Docker (optional)

### Environment setup

1. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in the required environment variables:

| Variable                | Description                               | Example value                                 |
|-------------------------|-------------------------------------------|-----------------------------------------------|
| `BOT_TOKEN`             | Telegram bot token from @BotFather        | `1234567890:AAE...`                           |
| `TONCENTER_API_KEY`     | TONCenter API key                         | `abcd1234efgh5678...`                         |
| `MYTONPROVIDER_API_KEY` | MyTONProvider API key                     | `abcd1234efgh5678...`                         |
| `DB_URL`                | Database connection string                | `sqlite+aiosqlite:///./data/database.sqlite3` |
| `REDIS_URL`             | Redis connection string for state storage | `redis://localhost:6379/0`                    |

### Run

#### Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Apply database migrations
alembic upgrade head

# Start the bot
python -m app
```

#### With Docker

```bash
# Start in background
docker-compose up -d

# View logs
docker-compose logs -f
```

## Development

### Project structure

```
    .
    ├── app/                                # Main application
    │   ├── alert/                          # Alerts system
    │   ├── api/                            # External APIs
    │   │   ├── mytonprovider/              # MyTONProvider API wrapper
    │   │   └── toncenter/                  # TONCenter API wrapper
    │   ├── bot/                            # Telegram bot
    │   │   ├── dialogs/                    # Dialogs and states
    │   │   ├── handlers/                   # Event handlers
    │   │   ├── middlewares/                # Middleware
    │   │   ├── utils/                      # Utilities
    │   │   └── commands.py                 # Bot commands
    │   ├── database/                       # Database
    │   │   ├── models/                     # SQLAlchemy models
    │   │   ├── repository.py               # Repository
    │   │   └── unitofwork.py               # Unit of Work pattern
    │   └── scheduler/                      # Task scheduler
    │       └── jobs/                       # Background jobs
    │           ├── sync_providers/         # Providers sync jobs
    │           ├── alerts_dispatch.py      # Processing and dispatching alerts
    │           ├── monthly_reports.py      # Monthly reports generation
    │           └── update_wallets.py       # Updating providers wallets data
    ├── alembic/                            # Database migrations
    ├── locales/                            # Localization files
    ├── data/                               # Database and service files
    └── docker-compose.yml                  # Docker configuration
```

### Integrations

* **MyTONProvider API** — provider data and telemetry
* **TONCenter API** — transactions, balances, and provider revenue

### Data models

* **ProviderModel** — provider information
* **ProviderHistoryModel** — provider history (archived state)
* **TelemetryModel** — current telemetry and metrics
* **TelemetryHistoryModel** — telemetry history snapshots
* **WalletModel** — provider wallet state
* **WalletHistoryModel** — wallet history (balance, earnings)
* **UserModel** — user data
* **UserSubscriptionModel** — user subscriptions
* **UserAlertSettingModel** — user alert preferences
* **UserTriggeredAlertModel** — triggered alerts log

### Task scheduler

* **sync_providers/update_providers** — provider sync and updates
* **sync_providers/update_telemetry** — telemetry collection and persistence
* **update_wallets** — wallets update and transaction sync
* **alerts_dispatch** — alert processing and dispatching
* **monthly_reports** — monthly reports generation

## License

This project is licensed under [Apache-2.0](LICENSE).

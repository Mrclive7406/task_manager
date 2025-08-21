# Task Manager

Простой менеджер задач, реализованный с использованием **FastAPI**, **SQLAlchemy**, **Pydantic** и **PostgreSQL/SQLite**.

Проект поддерживает создание, обновление, получение и удаление задач через REST API. Также настроен CI с GitHub Actions, проверкой линтером и запуском тестов.

## Особенности

- CRUD операции для задач
- Статусы задач: создано, в работе, завершено
- Валидация данных через Pydantic
- Асинхронный FastAPI сервер
- CI/CD с GitHub Actions (линтинг, тесты, coverage)


## Установка и запуск

1. Клонировать репозиторий:
git clone git@github.com:Mrclive7406/task_manager.git
cd task_manager

2.Создать виртуальное окружение и установить зависимости:

python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
pip install -r requirements.txt

3. Запуск сервера:

uvicorn app.main:app --reload

    Открыть документацию API:

    Swagger: http://127.0.0.1:8000/docs

    Redoc: http://127.0.0.1:8000/redoc
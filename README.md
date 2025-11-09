# Django Project

Apartment-store - Магазин квартир на Django с базовой структурой и настройками.

## Описание

Этот проект представляет собой веб-приложение Магазин квартир, построенное на фреймворке Django. Включает в себя основные настройки и структуру для быстрого начала разработки.

## Функциональность

- Базовая конфигурация Django проекта
- Настройки для разработки и production
- Структура приложений Django
- Конфигурация базы данных
- Статические файлы и медиа

## Установка и запуск

### Предварительные требования

- Python 3.8+
- Django 4.2+
- Виртуальное окружение - (рекомендуется)

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/romanmst1988/Django_roman.git
cd Django_roman
Создайте и активируйте виртуальное окружение:

bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
# или
venv\Scripts\activate  # для Windows
Установите зависимости:

bash
pip install -r requirements.txt
Примените миграции:

bash
python manage.py migrate
Создайте суперпользователя (опционально):

bash
python manage.py createsuperuser
Запустите сервер разработки:

bash
python manage.py runserver
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/

Структура проекта
text
Django_roman/
├── manage.py
├── requirements.txt
└── [project_name]/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
Разработка
Для внесения изменений в проект:

Создайте новую ветку для функциональности

Внесите необходимые изменения

Создайте pull request для ревью

Контакты
Roman - GitHub профиль: https://github.com/romanmst1988
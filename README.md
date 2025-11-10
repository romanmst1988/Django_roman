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

Что сделано:
- Добавлено приложение 'users' с кастомной моделью User (AbstractUser), регистрацией, логином и редактированием профиля.
- Настройки: AUTH_USER_MODEL добавлен; EMAIL_BACKEND настроен на console backend.
- users.urls добавлен в urlpatterns (path 'users/').
- Попытка автоматически добавить LoginRequiredMixin в views.py файлов, содержащих 'product' — проверь вручную.

Что нужно сделать локально:
1) Установить зависимости (если необходимо): Django и др.
2) Выполнить миграции:
   python manage.py makemigrations
   python manage.py makemigrations users
   python manage.py migrate
3) Создать суперпользователя:
   python manage.py createsuperuser
4) Запустить сервер:
   python manage.py runserver
5) Проверь работу регистрации: http://127.0.0.1:8000/users/register/
   Письма будут выводиться в консоль.

Если при миграциях возникнут ошибки — пришли вывод, я помогу исправить.

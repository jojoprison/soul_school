# Бэк-энд проекта на Django

Dockerfile данной части проекта отсутствует. Вся логика билда проекта происходит в docker/nginx/Dockerfile.

### Поднять локально

- `предварительно скопировать и настроить .env.tmp -> .env в корне проекта (опционально)`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py collectstatic`
- `python manage.py createsuperuser`
- `python manage.py runserver` (по умолчанию на 8000)

# Awesome Mailin'

This project is a full-stack web application for Mailing.
It includes a backend Django application for managing mailings and notifications, 
a Celery worker for handling background tasks, and a frontend React application 
for displaying mailing statistics.

## Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

locally:
- `git clone https://github.com/your_username/awesome_project.git`
- `cd back_end`
- `pip install poetry`
- `poetry install --no-dev`
- `python manage.py collectstatic --noinput`
- `python manage.py migrate`
- `python manage.py runserver 8000`

- `cd ..`
- `cd front_end`
- `npm start`

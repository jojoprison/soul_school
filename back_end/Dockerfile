FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy the current directory contents into the container at /app
COPY . /app

RUN poetry config virtualenvs.create false && \
    poetry install --only main

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start Django's development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
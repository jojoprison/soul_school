FROM python:3.10-slim
LABEL authors="jojoprison"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./back_end/pyproject.toml ./back_end/poetry.lock /app/back_end/

WORKDIR /app/back_end

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root

COPY ./back_end /app/back_end
COPY ./docker /app/docker

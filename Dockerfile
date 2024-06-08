FROM python:3.11.9 AS builder

ENV PYTHONUNBUFFERED=1 \ 
    PYTHONDONTWRITEBYTECODE=1 

RUN pip install poetry && poetry config virtualenvs.in-project true

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY app.py .

RUN poetry install

FROM python:3.11.9-slim


WORKDIR /app

COPY --from=builder /app .
COPY /static ./static/


CMD ["/app/.venv/bin/python", "app.py"]
FROM python:3.9-slim-buster AS builder

ARG POETRY_VERSION

WORKDIR /app

RUN python -m pip install --upgrade pip && \
    python -m pip install poetry==$POETRY_VERSION && \
    python -m venv /venv

COPY poetry.lock pyproject.toml ./

RUN . /venv/bin/activate && poetry install --only main --no-root

COPY . .

FROM python:3.9-slim-buster

WORKDIR /app

COPY --from=builder /venv /venv
COPY --from=builder /app /app

EXPOSE 5000

CMD . /venv/bin/activate && python3 -u app/main.py
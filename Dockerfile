FROM python:3.13-slim-bookworm
LABEL authors="aliamir"

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl procps


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml .
COPY uv.lock .

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "src/main.py"]

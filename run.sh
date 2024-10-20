#!/bin/sh
set -e
set -x

if [ "$ENV" = "local" ]; then
  poetry run uvicorn app.main:app --host 0.0.0.0 --port 80 --log-level info --forwarded-allow-ips "*" --reload
elif [ "$ENV" = "staging" ]; then
  alembic upgrade head
  uvicorn app.main:app --host 0.0.0.0 --port 80 --log-level info --forwarded-allow-ips "*"
elif [ "$ENV" = "production" ]; then
  alembic upgrade head
  uvicorn app.main:app --host 0.0.0.0 --port 80 --log-level info --forwarded-allow-ips "*"
fi
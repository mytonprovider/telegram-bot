#!/bin/sh
set -e

git config --global --add safe.directory /usr/src/app

alembic upgrade head

exec python -m app

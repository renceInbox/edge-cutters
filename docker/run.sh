#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

uvicorn --host $HOST --port $PORT "$APP_MODULE"

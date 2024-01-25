#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export APP_MODULE=${APP_MODULE-run:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

uvicorn  --bind $HOST:$PORT "$APP_MODULE"

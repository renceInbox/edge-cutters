#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Run migrations
#alembic upgrade head

exec "$@"

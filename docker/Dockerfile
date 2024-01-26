FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER_BUILDKIT 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system app && adduser --system --group app

WORKDIR /app

RUN rm -rf /var/lib/apt/lists/* && \
    apt-get purge --auto-remove && \
    apt-get clean

COPY ./requirements.txt /requirements.txt

RUN --mount=type=cache,target=/root/.cache \
    pip install -r /requirements.txt --no-cache-dir

COPY ./docker/run.sh /run.sh
RUN chmod +x /run.sh

COPY ./docker/prestart.sh /prestart.sh
RUN chmod +x /prestart.sh

COPY  --chown=app . /app

ENV PYTHONPATH=/app

USER app

ENTRYPOINT ["/prestart.sh"]

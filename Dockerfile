FROM python:3.9-alpine

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /usr/app

RUN addgroup -g 101 -S django && adduser -u 101 -D -S -G django django
RUN apk add --update --no-cache su-exec

# Set the time zone inside the container
RUN apk add tzdata --virtual .tzdata \
    && cp /usr/share/zoneinfo/Europe/Bucharest /etc/localtime \
    && echo "Europe/Bucharest" > /etc/timezone \
    && apk del .tzdata

# some packages have runtime dependencies on system libraries
RUN set -ex && apk add --no-cache libpq zlib-dev jpeg-dev

COPY poetry.lock pyproject.toml ./

# some packages need to be compiled from source and have build-time dependencies
RUN set -ex \
    && apk add --virtual .build-deps \
        gcc \
        build-base \
        musl-dev \
        libressl-dev \
        # these 2 are for postgres & gis
        python3-dev \
        libffi-dev \
        postgresql-dev \
        curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && export PATH="$HOME/.poetry/bin:$PATH" \
    && pip install --upgrade pip \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && pip install gunicorn whitenoise \
    && apk del .build-deps

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=main.settings.production

COPY src/ ./

RUN mkdir -p logs

COPY django-entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/django-entrypoint.sh
ENTRYPOINT [ "/usr/bin/django-entrypoint.sh" ]

# link image with github repo
LABEL org.opencontainers.image.source=https://github.com/dsc-upt/opportunity-backend

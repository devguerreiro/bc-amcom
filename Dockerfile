FROM python:3.10-alpine

ENV WORKDIR="/app"

WORKDIR ${WORKDIR}

RUN apk update && apk add gcc musl-dev libpq-dev

RUN pip3 install poetry

COPY pyproject.toml manage.py ${WORKDIR}/

RUN poetry export -f requirements.txt -o requirements.txt --without-hashes && pip3 install -r requirements.txt

ARG port=8000

ENV PORT=${port}

EXPOSE ${port}

ARG username="admin"
ARG password="admin"

ARG db_name="dunder_mifflin"
ARG db_user="db_user"
ARG db_pass="db_pass"
ARG db_host="localhost"
ARG db_port="5432"

ENV DJANGO_SECRET_KEY="some_secret_key" \
    DJANGO_SUPERUSER_USERNAME=${username} \
    DJANGO_SUPERUSER_PASSWORD=${password} \
    DJANGO_DB_NAME=${db_name} \
    DJANGO_DB_USER=${db_user} \
    DJANGO_DB_PASS=${db_pass} \
    DJANGO_DB_HOST=${db_host} \
    DJANGO_DB_PORT=${db_port}

COPY entrypoint.sh ${WORKDIR}/

COPY dunder_mifflin ${WORKDIR}/dunder_mifflin/

ENTRYPOINT ["./entrypoint.sh"]

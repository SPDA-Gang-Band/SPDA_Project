FROM python:latest

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install --upgrade pip && python -m pip install pip-tools
RUN pip-compile && pip-sync

RUN python manage.py runserver
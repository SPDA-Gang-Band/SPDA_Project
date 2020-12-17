###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.5-alpine as builder

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && pip3 install --upgrade pip
RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev
RUN apk add libjpeg-turbo pcre
RUN apk add build-base
# lint
RUN pip install --upgrade pip
RUN pip install flake8
RUN pip install cffi

COPY . .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/backend/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.8.5-alpine

# create directory for the app user
RUN mkdir -p /home/SPDA_Project

# create the app user
RUN addgroup -S app && adduser -S app -G app



# create the appropriate directories
ENV HOME=/home/SPDA_Project
ENV APP_HOME=/home/SPDA_Project/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME


# install dependencies
RUN apk update && apk add libpq
RUN apk add jpeg-dev zlib-dev
RUN apk add libjpeg-turbo pcre
RUN apk add libffi-dev
COPY --from=builder /usr/src/SPDA_Project/wheels /wheels
COPY --from=builder /usr/src/SPDA_Project/requirements.txt .
RUN pip install --no-cache /wheels/*



# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/SPDA_Project/web/entrypoint.sh"]
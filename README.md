# SPDA-Project
# Module for registration/editing applications for external training

## Requirements

Python 3.8

**pip-tools** is used for the management of requirements: https://github.com/jazzband/pip-tools.

#### How to add a new dependency?

1. Add new requirements in `requirements.in`.
2. Run ``pip-compile``, requirements.txt is updated automatically
3. Run ``pip-sync``, new packages are installed

## Endpoints description
* `http://127.0.0.1:8000/swagger/`

## To run server locally use this command
* `py manage.py runserver`
### Run database migrations
* `py manage.py migrate`

### Database configuration
If you don't want to configure postgresql database. You can comment DATABASES in settings.py and uncomment DATABASES below. Now server will use sqlite 

## Authentication is done using a header
Header should look like that: `fullname 'user_name' 'user_surname'`
If there is no user with this name new user will be created

## Deploy
For deployment we use docker-compose. To run this project using dockeryou need:
1. clone both backend and frontend repositories in one directory
2. move file `docker-compose.back_and_front.yml` in this directory with 2 repositories.
3. run command `sudo docker-compose -f docker-compose.back_and_front.yml up -d --build`
4. Don't forget to run migrations and collect static:
`sudo docker-compose -f docker-compose.back_and_front.yml exec web python manage.py migrate --noinput`
`sudo docker-compose -f docker-compose.back_and_front.yml exec web python manage.py collectstatic --no-input --clear`

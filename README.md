# Django 2.2 LTS Project 
## To run
### Create a virtualenv environment
Install in Debian based distributions 

`apt install python3-pip virtualenv python3-dev default-libmysqlclient-dev build-essential`

Create virtualenv

`virtualenv -p python3 venv`

Set virtualenv environment

`. venv/bin/activate`

### Install dependencies with pip
`pip install -r requirements.txt`

### Migrate database

Make migrations

`python3 manage.py makemigrations`

Run migrate

`python manage.py migrate`

Run server

`python manage.py runserver`

Home: http://localhost:8000

Admin: http://localhost:8000/admin

## Requirements

- Django 2.2 [Release Note](https://docs.djangoproject.com/en/2.2/releases/2.2/)
- Bootstrap 4
- Virtualenv

See [requirements.txt](requirements.txt)

## Docs

- [Quick start Django](https://www.djangoproject.com/start/)

# Django 2.2 LTS Project

Development project with Django 2.2 LTS using MVT (Model, View and Template) to course.
- Auth
- Templates
- Models
- URLs patterns

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

- Python 3.5 (see release note) or higher (3.9 as of 2.2.17)
- Django 2.2 - [Release Note](https://docs.djangoproject.com/en/2.2/releases/2.2/)
- Bootstrap 4
- Virtualenv
- SQL Lite Browser (project uses sqlite3)

See [requirements.txt](requirements.txt)

## Docs

- [Quick start Django](https://www.djangoproject.com/start/)

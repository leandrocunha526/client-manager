# Client manager project with Django 4.2.x LTS

[![Django CI](https://github.com/leandrocunha526/client-manager/actions/workflows/django.yml/badge.svg)](https://github.com/leandrocunha526/client-manager/actions/workflows/django.yml)

Development project with Django 4.2.x LTS using design pattern MVT (Model, View and Template) to course.

## About

Project to assist in the products and customers management. It was used in Gregorio Pacheco's Udemy Django course and modified by Leandro Cunha.

## Features

- Admin: One of the most powerful parts of Django is its automatic admin interface. It reads metadata in your models to provide a powerful and production-ready interface that content producers can immediately use to start managing content on your site. It’s easy to set up and provides many hooks for customization.
- Auth: Django comes with a full-featured and secure authentication system. It handles user accounts, groups, permissions and cookie-based user sessions. This lets you easily build sites that allow users to create accounts and safely log in/out.
- URLs patterns and views: A clean, elegant URL scheme is an important detail in a high-quality web application. Django encourages beautiful URL design and doesn’t put any cruft in URLs, like .php or .asp. To design URLs for an application, you create a Python module called a URLconf. Like a table of contents for your app, it contains a simple mapping between URL patterns and your views.
- Forms: Django provides a powerful form library that handles rendering forms as HTML, validating user-submitted data, and converting that data to native Python types. Django also provides a way to generate forms from your existing models and use those forms to create and update data.
- ORM: Deﬁne your data models entirely in Python. You get a rich, dynamic database-access API for free but you can still write SQL if needed.
- Templates: Django’s template language is designed to strike a balance between power and ease. It’s designed to feel comfortable and easy-to-learn to those used to working with HTML, like designers and front-end developers. But it is also flexible and highly extensible, allowing developers to augment the template language as needed.
- Models: A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
- Internationalization: Django offers full support for translating text into different languages, plus locale-specific formatting of dates, times, numbers, and time zones. It lets developers and template authors specify which parts of their apps should be translated or formatted for local languages and cultures, and it uses these hooks to localize web applications for particular users according to their preferences.

## How it works

![Django](https://www.horadecodar.com.br/wp-content/uploads/2019/01/django-r-r.jpg)

## How to run

### Create a environment with virtualenv

Install in Debian based distributions:

`apt install python3-pip virtualenv`

Install in Arch based distributions:

`pacman -S virtualenv python-pip`

Create virtualenv:

`virtualenv -p python3 venv`

Set virtualenv environment:

`. venv/bin/activate`

Install dependencies with pip:
`pip install -r requirements.txt`

### Migrate database

Make migrations:

Create folders in clients and product with migration name create file `__init__.py`.

`python3 manage.py makemigrations`

If you do not carry out the above process, the migrations will not be created and the project will have a 500 internal server error.

Run migrate:

`python manage.py migrate`

Run server:

`python manage.py runserver`

Link: <http://localhost:8000>

Admin: <http://localhost:8000/admin>

OBS: To access Django Admin only create user with: `python manage.py createsuperuser`.

## Requirements

- Python 3.8 (see release note) or higher
- Django 4.2.x LTS - [Release Notes](https://docs.djangoproject.com/en/4.2/releases)
- Bootstrap 4
- Virtualenv
- SQL Lite Browser (project uses sqlite3) to development environment.
- PostgreSQL

See [requirements.txt](requirements.txt)

## Docs

- [Quick start Django](https://www.djangoproject.com/start/)

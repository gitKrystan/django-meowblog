# Meow Blog

##### By Krystan Menne

Meow Blog is a blog for cats.

## Prerequisites
* Python 3.5
* Pip
* PostgreSQL

## Installation/Setup
1. Clone repository

  ```
  $ git clone https://github.com/gitKrystan/django-meowblog.git
  $ cd django-meowblog
  ```

1. Create and activate your virtual environment (using virtualenv or equivalent)

1. Install requirements

  ```
  $ pip install -r requirements.txt
  $ npm install
  ```

1. Create your database

  ```
  $ psql
  # CREATE USER root;
  # ALTER USER root CREATEDB;
  # CREATE DATABASE meowblog OWNER root;
  # \q
  ```
1. Run migrations

  ```
  $ python manage.py migrate
  ```
1. Create superuser

  `$ python manage.py createsuperuser` then follow prompts

1. Seed database

  `$ python manage.py loaddata seed.json`

## Running / Development
1. `$ python manage.py runserver `
1. Visit your app at http://localhost:8000

## Running Tests
`$ python manage.py test`

## License
Copyright (c) 2016 Krystan Menne
This software is licensed under the MIT license.

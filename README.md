# Meow Blog

##### By Krystan Menne

Meow Blog is a blog for cats.

## Prerequisites
* Python 3.5
* Pip
* PostgreSQL

## Installation/Setup
1. Clone repository and install requirements

  ```
  $ git clone https://github.com/gitKrystan/django-meowblog.git`
  $ cd django-meowblog
  $ pip install -r requirements.txt
  $ npm install
  ```
1. Create your database

  ```
  $ psql
  # CREATE USER root;
  # ALTER USER root CREATEDB;
  # CREATE DATABASE meowblog OWNER name;
  # \q
  ```
1. Run migrations

  ```
  $ python manage.py migrate
  ```
1. Create superuser

  `$ python manage.py createsuperuser` then follow prompts

## Running / Development
1. `$ python manage.py runserver `
1. Visit your app at http://localhost:8000

## Running Tests
`$ python manage.py test`

## License
Copyright (c) 2016 Krystan Menne
This software is licensed under the MIT license.

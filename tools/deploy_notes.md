## Deployment Notes

1. Get Python3, Nginx, Pip3, virtualenv, virtualenvwrapper, mysql-client
    Maybe also libmysqlclient-dev

2. With virtualenvwrapper, install requirements.

3. Set environmental variables:
  * SECRET_KEY
  * DJANGO_SETTINGS_MODULES
  * DB_NAME, DB_USER, DB_PASSWORD

4. Set MYSQL user and password.
  * manage.py check
  * manage.py migrate

5. Set static options and collectstatic.

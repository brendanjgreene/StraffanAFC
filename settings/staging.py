from base import *
import dj_database_url

DEBUG = False

SECRET_KEY = 'SECRET_KEY'

INSTALLED_APPS.append('storages')

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")

# uncomment the below line if the above line is not working
# DATABASES['default'] = dj_database_url.parse("mysql://bf4174401dd1d4:3eb1be20@eu-cdbr-west-01.cleardb.com/heroku_a77520ba3d93d67?")

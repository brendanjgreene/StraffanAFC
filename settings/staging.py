from base import *
import dj_database_url
import settings

DEBUG = False

INSTALLED_APPS.append('storages')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://bf4174401dd1d4:3eb1be20@eu-cdbr-west-01.cleardb.com/heroku_a77520ba3d93d67?reconnect=true")

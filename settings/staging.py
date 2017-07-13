from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://ba2db3b0c1d81f:654a3797@eu-cdbr-west-01.cleardb.com/heroku_00b5e60d3f182f9?reconnect=true")

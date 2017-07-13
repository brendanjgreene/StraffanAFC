from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://bce8728ef94639:dec5b67a@eu-cdbr-west-01.cleardb.com/heroku_54ef77cf2eb9b46?reconnect=true")
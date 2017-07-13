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
    "mysql://b9ea85138f376b:5e9d7db4@eu-cdbr-west-01.cleardb.com/heroku_c94194baf431fad?reconnect=true")
#  mysql://b9ea85138f376b:5e9d7db4@eu-cdbr-west-01.cleardb.com/heroku_c94194baf431fad?

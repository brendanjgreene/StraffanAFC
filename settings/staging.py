from base import *
import dj_database_url

DEBUG = False

SECRET_KEY = 'SECRET_KEY'

INSTALLED_APPS.append('storages')

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# delete this if s3 not functioning properly
AWS_STORAGE_BUCKET_NAME = 'straffanafcmedia'
AWS_ACCESS_KEY_ID = 'AKIAIKU3ZDH34T62BTTA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# delete

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")

# uncomment the below line if the above line is not working
# DATABASES['default'] = dj_database_url.parse("mysql://bf4174401dd1d4:3eb1be20@eu-cdbr-west-01.cleardb.com/heroku_a77520ba3d93d67?")


# DO NOT DO THIS! delete if doesnt work
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_ROOT = 'storages.backends.s3boto.S3BotoStorage'
#  delete

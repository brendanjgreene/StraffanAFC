from base import *
import dj_database_url

DEBUG = False

SECRET_KEY = 'SECRET_KEY'

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# THIS IS OK BECAUSE I AM USING AWS FOR MEDIAFILES ONLY!
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME 
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")

# uncomment the below line if the above line is not working
# DATABASES['default'] = dj_database_url.parse("mysql://bf4174401dd1d4:3eb1be20@eu-cdbr-west-01.cleardb.com/heroku_a77520ba3d93d67?")

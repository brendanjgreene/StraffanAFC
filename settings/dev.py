from base import *
from secret import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware',)

# THIS IS OK BECAUSE I AM USING AWS FOR MEDIAFILES ONLY!
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

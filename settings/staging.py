from base import *
import dj_database_url

DEBUG = False

DATABASES['default'] = dj_database_url.parse(
    "mysql://bf4174401dd1d4:3eb1be20@eu-cdbr-west-01.cleardb.com/heroku_a77520ba3d93d67?reconnect=true")

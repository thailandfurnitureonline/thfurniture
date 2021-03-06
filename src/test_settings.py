# this is an extremely simple Satchmo standalone store.

import logging
import os, os.path

from settings import *

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG
NO_STOCK_CHECKOUT = True

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)

DIRNAME = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = '/opt/thai/media/'
STATIC_ROOT = '/opt/thai/static/'


SATCHMO_DIRNAME = DIRNAME
    
gettext_noop = lambda s:s

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
   ('en', gettext_noop('English')),
   ('th', gettext_noop('Thai')),
)

#These are used when loading the test data
SITE_NAME = "simple"

DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'ado_mssql'.
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(DIRNAME, 'simple.db'),  # Or path to database file if using sqlite3
        #'USER': '',             # Not used with sqlite3.
        #'PASSWORD': '',         # Not used with sqlite3.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'site1',             # Not used with sqlite3.
        'PASSWORD': 'qwerty',         # Not used with sqlite3
        'NAME': 'websitedb',
        'HOST': 'localhost',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'liusdhflawhtp934yt09aw4ypgoa4whgp9a4w8ygp04w8ytp0y'

##### For Email ########
# If this isn't set in your settings file, you can set these here
#EMAIL_HOST = 'host here'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'your user here'
#EMAIL_HOST_PASSWORD = 'your password'
#EMAIL_USE_TLS = True

#These are used when loading the test data
SITE_DOMAIN = "thailandfurnitureonline.com"
SITE_NAME = "Thailand Furniture Online"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "Z"

ACCOUNT_ACTIVATION_DAYS = 7

INSTALLED_APPS += (
    'gunicorn',
)

#Configure logging
LOGFILE = "/opt/thai/logs/satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(DIRNAME,LOGFILE),
                    filemode='w')

logging.getLogger('django.db.backends').setLevel(logging.INFO)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.getLogger('suds').setLevel(logging.INFO)
logging.info("Satchmo Started")


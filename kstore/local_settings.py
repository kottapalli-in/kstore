# this is an extremely simple Satchmo standalone store.

import logging
import os, os.path

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)

DIRNAME = os.path.dirname(os.path.abspath(__file__))
REPOROOT = os.path.dirname(DIRNAME)

SATCHMO_DIRNAME = DIRNAME
    
gettext_noop = lambda s:s

LANGUAGE_CODE = 'te'
LANGUAGES = (
   ('te', gettext_noop('Telugu')),
)

#These are used when loading the test data
SITE_NAME = "simple"

DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'ado_mssql'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(REPOROOT, 'kstore.db'),  # Or path to database file if using sqlite3
        #'USER': '',             # Not used with sqlite3.
        #'PASSWORD': '',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'EXAMPLE SECRET KEY'

##### For Email ########
# If this isn't set in your settings file, you can set these here
#EMAIL_HOST = 'host here'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'your user here'
#EMAIL_HOST_PASSWORD = 'your password'
#EMAIL_USE_TLS = True

#These are used when loading the test data
SITE_DOMAIN = "shop.kottapalli.in"
SITE_NAME = "Kottapalli Book Store"

# not suitable for deployment, for testing only, for deployment strongly consider memcached.
CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "Z"

ACCOUNT_ACTIVATION_DAYS = 7

#Configure logging
LOGFILE = "satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(REPOROOT,LOGFILE),
                    filemode='w')

logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)
logging.info("Satchmo Started")


L10N_SETTINGS = {
  'currency_formats' : {
     'INR' : {'symbol': u'Rs.', 'positive' : u"Rs. %(val)0.2f", 'negative': u"Rs. (%(val)0.2f)",
               'decimal' : '.'},
  },
  'default_currency' : 'INR',
  'show_admin_translations': False,
  'allow_translation_choice': False,
}

# required to run Django app to run at /
FORCE_SCRIPT_NAME = ""

BANK_ACCOUNT_DETAILS = '''
Account Name: Kottapalli,
Account Number: 0123456789,
Account Branch: SBI,
Branch Address: Kottapalli,
IFSC Code: 12345
'''

# Hook to get production settings
try:
    from production_settings import *
except ImportError:
    pass

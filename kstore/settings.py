# Django settings for satchmo project.
# This is a recommended base setting for further customization
import os

DIRNAME = os.path.dirname(__file__)

DJANGO_PROJECT = 'kstore'
DJANGO_SETTINGS_MODULE = 'kstore.settings'

ADMINS = (
     ('', ''),         # tuple (name, email) - important for error reports sending, if DEBUG is disabled.
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# Image files will be stored off of this path
#
# If you are using Windows, recommend using normalize_path() here
#
# from satchmo_utils.thumbnail import normalize_path
# MEDIA_ROOT = normalize_path(os.path.join(DIRNAME, 'static/'))
MEDIA_ROOT = os.path.join(DIRNAME, 'static')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL="/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z^71^zh+64dxc7xwao(olj)sm78qkj)s6p-p)qlb+3mvj^_elz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    #"satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#this is used to add additional config variables to each request
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = ('satchmo_store.shop.context_processors.settings',
                               'django.contrib.auth.context_processors.auth',
                               'kstore.context_processors.theme',
                               'kstore.context_processors.bank_account_details',
                               'kstore.context_processors.search_query',
                               'kstore.context_processors.kfeeds',
                               #'satchmo_ext.recentlist.context_processors.recent_products',
                               )

ROOT_URLCONF = 'kstore.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sites',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'registration',
    'sorl.thumbnail',
    'keyedcache',
    'livesettings',
    'l10n',
    'satchmo_utils.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    #'satchmo_store.contact.supplier',
    #'shipping.modules.tiered',
    #'satchmo_ext.newsletter',
    #'satchmo_ext.recentlist',
    #'testimonials',         # dependency on  http://www.assembla.com/spaces/django-testimonials/
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    #'product.modules.downloadable',
    #'product.modules.subscription',
    #'satchmo_ext.product_feeds',
    #'satchmo_ext.brand',
    'payment',
    #'payment.modules.dummy',
    'payment.modules.cod',
    'kstore.offline_payment',
    #'payment.modules.giftcertificate',
    #'satchmo_ext.wishlist',
    #'satchmo_ext.upsell',
    #'satchmo_ext.productratings',
    'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    #'shipping.modules.tieredquantity',
    #'satchmo_ext.tieredpricing',
    #'typogrify',            # dependency on  http://code.google.com/p/typogrify/
    #'debug_toolbar',
    'app_plugins',
    'kstore.dashboard',
    'kstore.tags',
)

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS' : False,
#}

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE' : '',
    'MULTISHOP' : False,
    'PRODUCT_SLUG': 'books',
    'CUSTOM_SHIPPING_MODULES': ['satchmo_indiapost']
    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

LIVESETTINGS_OPTIONS = {   
    1: {   
        'DB': False,
       'SETTINGS': {   
           'PAYMENT': {   
               'ALLOW_URL_REBILL': u'True',
               'LIVE': u'True',
                'ORDER_EMAIL_OWNER': u'True',
                'USE_DISCOUNTS': u'False'
            },
            'PAYMENT_PURCHASEORDER': {   
                'EXTRA_LOGGING': u'True',
                'LIVE': u'True'
            },
            'PAYMENT_COD': {   
                u'EXTRA_LOGGING': u'True',
                u'LABEL': u'Payment on Delivery',
                u'LIVE': u'True'
            },
            'PAYMENT_OFFLINE_PAYMENT': {   
                u'EXTRA_LOGGING': u'True',
                u'LABEL': u'Offline Bank Transfer',
                u'LIVE': u'True'
            },
            'PRODUCT': {   
                'MEASUREMENT_SYSTEM': u'["metric"]',
                'NO_STOCK_CHECKOUT': u'False'
            },
            'SHIPPING': {  
                'MODULES': u'["satchmo_indiapost"]'
            },
            'SHOP': {   
                'REQUIRED_BILLING_DATA': u'["email", "first_name", "last_name", "phone", "street1", "city", "postal_code", "country"]',
                'REQUIRED_SHIPPING_DATA': u'["addressee", "street1", "city", "postal_code", "country"]'
            },
           'satchmo_indiapost': {   
             #  'SHIPPING_CHOICES': u'["REG_PARCEL", "REG_PARCEL_VPP", "REG_BOOKPOST", "REG_BOOKPOST_VPP"]',
               'SHIPPING_CHOICES': u'["REG_BOOKPOST", "REG_BOOKPOST_VPP"]',
               'VERBOSE_LOG': u'True'
            }
        }
    }
}

SKIP_SOUTH_TESTS=True

LOCALE_PATHS = (
    'locale'
)

# Load the local settings
from local_settings import *


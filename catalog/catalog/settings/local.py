from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ('django.contrib.admin', 'debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1')
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

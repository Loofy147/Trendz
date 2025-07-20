from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']  # Add your production domain here

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'MAX_CONNS': 20,
            'MIN_CONNS': 5,
        },
        'CONN_MAX_AGE': 600,  # Connection persistence
    }
}

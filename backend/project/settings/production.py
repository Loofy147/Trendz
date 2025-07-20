from .base import *
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']  # Add your production domain here

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

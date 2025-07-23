from .base import *
import dj_database_url

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["your-production-domain.com"]  # Add your production domain here


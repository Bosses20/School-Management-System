from .base import *
import os
import dj_database_url

# Render deployment settings
DEBUG = False

# Render provides DATABASE_URL
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Allow Render hosts
ALLOWED_HOSTS = ['*']  # Render will handle the domain
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
]

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Disable Redis for basic deployment (use database cache)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
    }
}

# Create cache table on first run
# python manage.py createcachetable

# Disable some features for basic deployment
USE_PAYMENT_OPTIONS = False
USE_STRIPE = False
USE_SENTRY = False
USE_MAILCHIMP = False

# Simple email backend for now
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable Celery for basic deployment
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Override environment variables that might cause issues
try:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-render-deployment-key-change-in-production')
    TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')
except:
    SECRET_KEY = 'django-insecure-render-deployment-key-change-in-production'
    TIME_ZONE = 'UTC'
from .base import *
import os

# PythonAnywhere deployment settings
DEBUG = False

# PythonAnywhere MySQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'your_username$school_management'),
        'USER': os.environ.get('DB_USER', 'your_username'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'your_password'),
        'HOST': os.environ.get('DB_HOST', 'your_username.mysql.pythonanywhere-services.com'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Allow PythonAnywhere hosts
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://*.pythonanywhere.com',
]

# Static files for PythonAnywhere
STATIC_ROOT = '/home/yourusername/mysite/static'
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = '/home/yourusername/mysite/media'
MEDIA_URL = '/media/'

# Use database cache (no Redis needed)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
    }
}

# Disable features that need external services
USE_PAYMENT_OPTIONS = False
USE_STRIPE = False
USE_SENTRY = False
USE_MAILCHIMP = False

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable Celery
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Simple secret key for demo
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-pythonanywhere-demo-key')
TIME_ZONE = 'UTC'
from .base import *
import os

# Railway deployment settings
DEBUG = False

# Railway provides DATABASE_URL
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

# Railway provides REDIS_URL
if 'REDIS_URL' in os.environ:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': os.environ.get('REDIS_URL'),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        },
    }

# Allow Railway hosts
ALLOWED_HOSTS = ['*']  # Railway will handle the domain
CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
    'https://*.up.railway.app',
]

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

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
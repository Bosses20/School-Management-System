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

# Remove problematic middleware for basic deployment
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Remove apps that might cause issues
INSTALLED_APPS = [
    'django_school_management.accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Local apps
    'django_school_management.students.apps.StudentsConfig',
    'django_school_management.teachers.apps.TeachersConfig',
    'django_school_management.result.apps.ResultConfig',
    'django_school_management.academics.apps.AcademicsConfig',
    'django_school_management.pages.apps.PagesConfig',
    'django_school_management.articles.apps.ArticlesConfig',
    'django_school_management.institute.apps.InstituteConfig',
    'django_school_management.curriculum.apps.CurriculumConfig',
    'django_school_management.payments.apps.PaymentsConfig',
    'django_school_management.notices.apps.NoticesConfig',
    
    # Essential third party apps
    'rest_framework',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap4',
    'rolepermissions',
    'taggit',
    'django_extensions',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'ckeditor_uploader',
    'mptt',
    'widget_tweaks',
    'django_social_share',
    'django_countries',
    'import_export',
    'django_tables2',
    'bootstrap4',
    'django_file_form',
    'tinymce',
    'drf_yasg',
    'django_rest_passwordreset',
]

# Disable some features for basic deployment
USE_PAYMENT_OPTIONS = False
USE_STRIPE = False
USE_SENTRY = False
USE_MAILCHIMP = False

# Simple email backend for now
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Override environment variables that might cause issues
try:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-render-deployment-key-change-in-production')
    TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')
except:
    SECRET_KEY = 'django-insecure-render-deployment-key-change-in-production'
    TIME_ZONE = 'UTC'
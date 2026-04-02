#!/usr/bin/env python
"""
Simple deployment script to create a superuser and load initial data
"""
import os
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
    django.setup()
    
    # Create superuser if it doesn't exist
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            email='admin@schoolmanagement.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("Superuser created successfully!")
    else:
        print("Superuser already exists!")
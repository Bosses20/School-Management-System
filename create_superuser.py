#!/usr/bin/env python
import os
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.railway')
    django.setup()
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            email='admin@schoolmanagement.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("✅ Superuser created successfully!")
        print("Email: admin@schoolmanagement.com")
        print("Password: admin123")
    else:
        print("ℹ️ Superuser already exists!")
#!/bin/bash

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create superuser if needed
python deploy.py

# Start the server
gunicorn config.wsgi --bind 0.0.0.0:$PORT
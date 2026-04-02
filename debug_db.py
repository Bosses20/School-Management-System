#!/usr/bin/env python
import os
import dj_database_url

print("=== DATABASE DEBUG INFO ===")
print(f"DATABASE_URL exists: {'DATABASE_URL' in os.environ}")
print(f"DATABASE_URL value: {os.environ.get('DATABASE_URL', 'NOT SET')[:50]}...")
print(f"Internal_Database_URL exists: {'Internal_Database_URL' in os.environ}")
print(f"Internal_Database_URL value: {os.environ.get('Internal_Database_URL', 'NOT SET')[:50]}...")

db_url = os.environ.get('DATABASE_URL') or os.environ.get('Internal_Database_URL')
if db_url:
    parsed = dj_database_url.parse(db_url)
    print(f"Parsed database config:")
    print(f"  ENGINE: {parsed.get('ENGINE')}")
    print(f"  NAME: {parsed.get('NAME')}")
    print(f"  USER: {parsed.get('USER')}")
    print(f"  HOST: {parsed.get('HOST')}")
    print(f"  PORT: {parsed.get('PORT')}")
else:
    print("No DATABASE_URL found, using fallback values:")
    print(f"DB_NAME: {os.environ.get('DB_NAME', 'NOT SET')}")
    print(f"DB_USER: {os.environ.get('DB_USER', 'NOT SET')}")
    print(f"DB_HOST: {os.environ.get('DB_HOST', 'NOT SET')}")
    print(f"DB_PASSWORD: {'SET' if os.environ.get('DB_PASSWORD') else 'NOT SET'}")

print("=== DJANGO SETTINGS MODULE ===")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')}")
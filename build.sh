#!/usr/bin/env bash

pip install -r requirements.txt


# Apply DB changes
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py migrate records 0002 --fake

# Collect static files
python manage.py collectstatic --noinput

# Create superuser (if it doesn't already exist)
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpass")
    print("Superuser created")
else:
    print("Superuser already exists")
END

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.dev")
django.setup()

from django.db.utils import IntegrityError
from administration.models import User

USERNAME = 'admin'
EMAIL = 'admin@example.com'
PASSWORD = 'admin'

try:
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
except IntegrityError:
    print(f"User '{USERNAME} <{EMAIL}>' already exists")
else:
    print(f"Created superuser '{USERNAME} <{EMAIL}>' with password '{PASSWORD}'")

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

USERNAME = "admin"
EMAIL = "admin@example.com"
PASSWORD = "admin"

try:
    get_user_model().objects.create_superuser(USERNAME, EMAIL, PASSWORD)
except IntegrityError:
    print("User '%s <%s>' already exists" % (USERNAME, EMAIL))
else:
    print("Created superuser '%s <%s>' with password '%s'" % (USERNAME, EMAIL, PASSWORD))

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

username = 'admin'
email = 'admin@example.com'
password = 'admin'

try:
    get_user_model().objects.create_superuser(username, email, password)
except IntegrityError:
    print("User '%s <%s>' already exists" % (username, email))
else:
    print("Created superuser '%s <%s>' with password '%s'" % (username, email, password))

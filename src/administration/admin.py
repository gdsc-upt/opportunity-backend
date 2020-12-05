from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from administration.models import User


@register(User)
class UserAdmin(BaseUserAdmin):
    pass

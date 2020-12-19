from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class AdministrationConfig(AppConfig):
    name = 'administration'


class CustomAdminConfig(AdminConfig):
    default_site = 'administration.admin_site.CustomAdminSite'

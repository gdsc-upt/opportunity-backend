"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from common.admin_site import admin_site
from utils import Config

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
CONFIG_FILE = os.path.join(BASE_DIR, "..", "config.yml")
config = Config(CONFIG_FILE)

admin_site.site_title = config.get("SITE_TITLE", "Django Template Project")
admin_site.site_header = config.get("SITE_HEADER", "Django Template Project")
SECRET_KEY = config.get("SECRET_KEY", raise_error=True)
DEBUG = config.get("DEBUG", False, cast=bool)
ALLOWED_HOSTS = config.get("ALLOWED_HOSTS", cast=list)

INSTALLED_APPS = [
    "administration",
    "website",
    "common",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "pwa",
    "corsheaders",
    "adminsortable2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config.get("DB_NAME", raise_error=True),
        "USER": config.get("DB_USER", default="root"),
        "PASSWORD": config.get("DB_PASSWORD", default="toor"),
        "HOST": config.get("DB_HOST", default="127.0.0.1"),
        "PORT": config.get("DB_PORT", default="5432", cast=int),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "administration.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Bucharest"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "/api/static/"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

#######################################
# CORS CONFIGS
CORS_ORIGIN_WHITELIST = (
    "http://localhost:4200",
    "https://opportunity.timis.tech",
    "https://dev.opportunity.timis.tech",
)
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = default_headers

#######################################
# THUMBNAIL CONFIGS
ADMIN_THUMBNAIL_STYLE = {
    "display": "block",
    "width": f"{config.get('THUMBNAIL_SIZE', default='200')}px",
    "height": "auto",
}
ADMIN_THUMBNAIL_BACKGROUND_STYLE = {"background": "#808080"}

SPECTACULAR_SETTINGS = {
    # path prefix is used for tagging the discovered operations.
    # use '/api/v[0-9]' for tagging apis like '/api/v1/albums' with ['albums']
    "SCHEMA_PATH_PREFIX": r"/api",
    # Dictionary of configurations to pass to the SwaggerUI({ ... })
    # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
    # 'SWAGGER_UI_SETTINGS': {
    #     'deepLinking': True,
    # },
    "SWAGGER_UI_FAVICON_HREF": "//unpkg.com/swagger-ui-dist@3.35.1/favicon-32x32.png",
    # General schema metadata. Refer to spec for valid inputs
    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#openapi-object
    "TITLE": admin_site.site_title + " API",
    "DESCRIPTION": "API Description",
    "TOS": None,
    # Optional: MAY contain 'name', 'url', 'email'
    "CONTACT": {
        "name": "Opportunity Dev Team",
    },
    # Optional: MUST contain 'name', MAY contain URL
    "LICENSE": {},
    "VERSION": "0.1.0",
    # Tags defined in the global scope
    # 'TAGS': [],
    # # Optional: MUST contain 'url', may contain 'description'
    # 'EXTERNAL_DOCS': {},
}

MAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "testbackendemail001@gmail.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "testbackendemail001@gmail.com"
EMAIL_HOST_PASSWORD = "Testemail001#"
EMAIL_USE_TLS = True

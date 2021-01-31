import os
from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from common.admin_site import admin_site
from main.settings import Config

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
    "drf_spectacular",
    "corsheaders",
    "adminsortable2",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

# required by allauth
SITE_ID = 1

REST_USE_JWT = True
JWT_AUTH_COOKIE = "jwt-auth"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
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
        "NAME": "django.contrib.auth"
        ".password_validation.UserAttributeSimilarityValidator",
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

JAZZMIN_SETTINGS = {
    # title of the window
    # (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Opportunity Admin Page",
    # Title on the brand, and login screen (19 chars max)
    # (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Opportunity",
    # square logo to use for your site, must be present in static files,
    # used for favicon and brand on top left
    # "site_logo": "img/logo.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to Opportunity!",
    # Copyright on the footer
    "copyright": "Opportunity Team",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        {
            "name": "Swagger",
            "url": "/api/swagger",
            "new_window": True,
        },
        # model admin to link to (Permissions checked against model)
        # {'model': 'administration.User'},
        {"model": "common.Example"},
        # App with dropdown menu to all its models pages
        # (Permissions checked against models)
        {"app": "administration"},
        {"app": "common"},
    ],
    #############
    # User Menu #
    ############
    # Additional links to include in the user menu on the top right
    # ("app" url type is not allowed)
    "usermenu_links": [{"model": "administration.user"}],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "administration": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
            }
        ]
    },
    # Custom icons for side menu apps/models
    # See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": "css/custom.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "administration.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "testbackendemail001@gmail.com"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "testbackendemail001@gmail.com"
EMAIL_HOST_PASSWORD = "Testemail001#"
EMAIL_USE_TLS = True

# DJANGO ALL AUTH SETTINGS
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

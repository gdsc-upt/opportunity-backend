import logging

from main.settings.base import *

INSTALLED_APPS += [
    "debug_toolbar",
    "nplusone.ext.django",
    "extra_checks",
]

MIDDLEWARE += [
    "nplusone.ext.django.NPlusOneMiddleware",
    "querycount.middleware.QueryCountMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# nplusone is a library for detecting the n+1 queries problem
# https://github.com/jmcarp/nplusone
NPLUSONE_LOGGER = logging.getLogger("nplusone")
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "nplusone": {
            "handlers": ["console"],
            "level": "WARN",
        },
    },
}

QUERYCOUNT = {
    "DISPLAY_DUPLICATES": 100,
    "IGNORE_SQL_PATTERNS": [r"django", r"auth"],
    "IGNORE_REQUEST_PATTERNS": [
        r"/serviceworker.js",
        r"/api/admin/jsi18n/",
        r"/media/*",
        r"/api/admin/$",
        r"/api/admin/login/",
        r"/manifest.json",
    ],
}

# used for django debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# django-extra-checks
# https://github.com/kalekseev/django-extra-checks
EXTRA_CHECKS = {
    "checks": [
        # Forbid `unique_together`:
        "no-unique-together",
        # Use the indexes option instead:
        "no-index-together",
        # Each model must be registered in admin:
        "model-admin",
        # FileField/ImageField must have non empty `upload_to` argument:
        "field-file-upload-to",
        # All model's fields must have verbose name.
        "field-verbose-name",
        # verbose_name must use gettext.
        "field-verbose-name-gettext",
        # Words in text wrapped with gettext must be in one case.
        "field-verbose-name-gettext-case",
        # help_text must use gettext.
        "field-help-text-gettext",
        # Text fields shouldn't use `null=True`:
        "field-text-null",
        # Prefer using BooleanField(null=True) instead of NullBooleanField:
        "field-boolean-null",
        # Don't pass `null=False` to model fields (this is django default)
        "field-null",
        # ForeignKey fields must specify db_index explicitly if used in
        # other indexes:
        {"id": "field-foreign-key-db-index", "when": "indexes"},
        # If field nullable `(null=True)`,
        # then default=None argument is redundant and should be removed:
        "field-default-null",
        # Fields with choices must have companion CheckConstraint
        # to enforce choices on database level
        "field-choices-constraint",
    ],
}

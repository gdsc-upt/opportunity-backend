from .base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

SILENCED_SYSTEM_CHECKS = [
    'security.W004',  # SECURE_HSTS_SECONDS
    'security.W008',  # SECURE_SSL_REDIRECT
    'security.W012',  # SESSION_COOKIE_SECURE
    'security.W016',  # CSRF_COOKIE_SECURE
]

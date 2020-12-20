from urllib.parse import urlparse

from .base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SILENCED_SYSTEM_CHECKS = [
    'security.W004',  # SECURE_HSTS_SECONDS
    'security.W008',  # SECURE_SSL_REDIRECT
]

#######################################
# PWA CONFIGS
PWA_APP_NAME = admin_site.site_title
PWA_APP_DESCRIPTION = 'Use it wisely!'
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/api/admin'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/api/admin'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/api/static/images/opportunity-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/api/static/images/opportunity-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/api/static/images/opportunity-1080x1080.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]

if not DEBUG:
    SWAGGER_SETTINGS = {
        'USE_SESSION_AUTH': False,
        'VALIDATOR_URL': None,
    }

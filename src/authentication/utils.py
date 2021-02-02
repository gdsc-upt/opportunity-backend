from importlib import import_module


def import_callable(path_or_callable):
    if hasattr(path_or_callable, "__call__"):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attr = path_or_callable.rsplit(".", 1)
        return getattr(import_module(package), attr)


def jwt_encode(user):
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

    refresh = TokenObtainPairSerializer.get_token(user)
    return refresh.access_token, refresh


try:
    from .jwt_auth import JWTCookieAuthentication
except ImportError:
    pass

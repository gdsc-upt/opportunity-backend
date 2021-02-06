def jwt_encode(user):
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

    refresh = TokenObtainPairSerializer.get_token(user)
    return refresh.access_token, refresh

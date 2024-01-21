from dj_rest_auth.serializers import LoginSerializer


class AppLoginSerializer(LoginSerializer):
    username = None

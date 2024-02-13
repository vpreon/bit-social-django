from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from accounts.models import User


class AppLoginSerializer(LoginSerializer):
    username = None


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',  'email', 'first_name', 'last_name', 'profile_image')
        read_only_fields = ('email',)

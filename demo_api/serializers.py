from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    username = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']



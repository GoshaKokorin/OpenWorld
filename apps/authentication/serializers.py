from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

from .models import EmailCode
from ..users.models import User


class EmailCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCode
        fields = ['email']


class VerifyCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = EmailCode
        fields = ['email', 'code']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['email', 'password', 'code']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if not email:
            raise serializers.ValidationError('The email should be only contain alphanumeric')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=64, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return {
            'email': user.email,
            'tokens': user.tokens,
        }
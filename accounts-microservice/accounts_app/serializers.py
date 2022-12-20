from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=300)


class DeletedSerializer(serializers.Serializer):
    deleted = serializers.BooleanField()

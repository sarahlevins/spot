from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = (
            'email',
            'nickname',
            'password',
        )

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

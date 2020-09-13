from rest_framework import serializers
from .models import Listing, Sighting

from datetime import datetime


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = (
            'latitude',
            'longitude',
            'description',
            'species',
        )
        read_only_fields = ('time', 'id')

    def create(self, validated_data):
        time = datetime.now()
        return Sighting.objects.create(**validated_data, time=time)

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            'description', instance.description)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get(
            'longitude', instance.longitude)
        instance.save()
        return instance


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'name',
            'time',
            'description',
            'user'
        )

    def create(self, validated_data):
        return Listing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            'description', instance.description)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

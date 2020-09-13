from .models import Listing, Sighting
from .serializers import ListingSerializer, SightingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SightingList(APIView):
    def get(self, request, format=None):
        sightings = Sighting.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = SightingSerializer(
            sightings, context=serializer_context, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SightingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingList(APIView):
    def get(self, request, format=None):
        listings = Listing.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = ListingSerializer(
            listings, context=serializer_context, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

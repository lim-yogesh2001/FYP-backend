
from django.shortcuts import render
from rest_framework.views import APIView
from .models import AboutUs, PrivacyPolicy, BookingPolicy
from .serializer import AboutSerializer, PrivacySerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AboutView(APIView):

    def get(self, request):
        try:
            about = AboutUs.objects.get(id=1)
            serializer = AboutSerializer(about)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AboutUs.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PrivacyView(APIView):

    def get(self, request):
        try:
            privacy = PrivacyPolicy.objects.get(id=1)
            serializer = PrivacySerializer(privacy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PrivacyPolicy.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class BookingPolicyView(APIView):

    def get(self, request):
        try:
            booking = BookingPolicy.objects.get(id=1)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookingPolicy.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

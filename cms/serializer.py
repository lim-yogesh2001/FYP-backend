from rest_framework import serializers
from .models import PrivacyPolicy, AboutUs, BookingPolicy

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPolicy
        fields = "__all__"
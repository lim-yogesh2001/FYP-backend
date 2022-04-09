from rest_framework import serializers
from .models import Theaters

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = "__all__"
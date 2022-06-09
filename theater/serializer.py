from rest_framework import serializers
from .models import Theaters, TheaterReviews

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theaters
        fields = "__all__"


class TheaterReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterReviews
        fields = ['id', 'ratings', 'comment', 'user_id']
        depth = 1

class TheaterWriteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterReviews
        fields = ['id', 'ratings', 'comment', 'theater_id', 'user_id']



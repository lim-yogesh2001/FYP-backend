from rest_framework import serializers
from .models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'movie_name', 'cover_image', 'release_date', 'genres',
                  'director', 'producers', 'casts', 'descripton', 'is_upcoming', 'is_popular']

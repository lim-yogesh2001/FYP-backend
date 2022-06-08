from rest_framework import serializers
from .models import Reserved_Seat, Seats, Shows, Tickets, Transection, MoviesWatched
from movie.models import Movies


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ['id', 'show_time', 'date',
                  'langauge', 'theater_id', 'movie_id', 'isHouseFull']
        depth = 1


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = "__all__"


class ReservedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserved_Seat
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = "__all__"

class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transection
        fields = "__all__"

class HistorOfMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'movie_name', 'cover_image', 'genres']

class MoviesWatchedSerializer(serializers.Serializer):
    movie_name = serializers.CharField(max_length=100)
    cover_image = serializers.ImageField()
    show_id = serializers.CharField(max_length=10)
    show_time = serializers.TimeField()
    date = serializers.DateField()
    theater_name = serializers.CharField(max_length=100)
    row = serializers.IntegerField(default=0)
    number = serializers.IntegerField(default=0)
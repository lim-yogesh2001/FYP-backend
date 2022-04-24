from rest_framework import serializers
from .models import Reserved_Seat, Seats, Shows, Tickets


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ['id', 'show_time', 'date',
                  'langauge', 'theater_id', 'movie_id']
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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from movie.models import Movies
from show.models import Reserved_Seat, Seats, Shows, Tickets
from show.serializer import ReservedSeatSerializer, SeatSerializer, ShowSerializer, TicketSerializer
from theater.models import Theaters

# Create your views here.


# //////    show APIView       ///////
class ShowsView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, movie_id):
        try:
            # to get list of shows based on movie_id
            movie = Movies.objects.get(id=movie_id)
            shows = Shows.objects.filter(movie_id=movie)
            serializer = ShowSerializer(shows, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response({"Not Found": "Show With that movie_id does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ShowsDetailView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, id):
        try:
            # to get the show detail of a show
            show = Shows.objects.get(id=id)
            serializer = ShowSerializer(show)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Shows.DoesNotExist:
            return Response({"Not Found": "Show with that id does not exist."}, status=status.HTTP_404_NOT_FOUND)

# /////////       show APIView       ///////////


# /////////       seat APIView       ///////////
class SeatView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            # to get the list of all the seats
            seats = Seats.objects.all()
            serializer = SeatSerializer(seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Seats.DoesNotExist:
            return Response({"Not Found": "Seats Not Found"}, status=status.HTTP_404_NOT_FOUND)


class TheaterSeatView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, theater_id):
        try:
            # to get the list of seats based on id of a theater
            theater = Theaters.objects.get(id=theater_id)
            seats = Seats.objects.filter(theater_id=theater)
            serializer = SeatSerializer(seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Theaters.DoesNotExist:
            return Response({"Not Found": "Seat for that theater_id does not exist"}, status=status.HTTP_404_NOT_FOUND)

# /////////       seat APIView       ///////////


# ////////        reserved seats     /////////
class ReservedSeatView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        # to get the reserved seat list
        try: 
            reserved_seats = Reserved_Seat.objects.all()
            serializer = ReservedSeatSerializer(reserved_seats, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Reserved_Seat.DoesNotExist:
            return Response({"Not Found": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        

# ////////        reserved seats     /////////


# ////////        ticket View       /////////
class TicketView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            tickets = Tickets.objects.all()
            serializer = TicketSerializer(tickets)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tickets.DoesNotExist:
            return Response({"Not Found": "Does Not Exist"}, status= status.HTTP_404_NOT_FOUND)

        
# ////////        ticket View       /////////








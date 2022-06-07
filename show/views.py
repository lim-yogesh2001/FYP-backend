import numpy as np
from os import stat
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status, permissions
from movie.models import Movies
from show.models import Reserved_Seat, Seats, Shows, Tickets, Transection, MoviesWatched
# , BookedTickets, ReservedTicket
from movie.serializers import MovieSerializer
from show.serializer import ReservedSeatSerializer, SeatSerializer, ShowSerializer, TicketSerializer, TransectionSerializer, HistorOfMoviesSerializer, MoviesWatchedSerializer
#  BookedTicketSerializer, ReservedTicketSerializer
from theater.models import Theaters
from accounts.models import User
# from hamro_cinema.FCMManager import send_booked_notification, send_reminder
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

    # renderer_classes = [JSONRenderer]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # to get the reserved seat list
        try:
            reserved_seats = Reserved_Seat.objects.all()
            serializer = ReservedSeatSerializer(reserved_seats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reserved_Seat.DoesNotExist:
            return Response({"Not Found": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args):
        serializer = ReservedSeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            show = Shows.objects.get(id=serializer.data['show_id'])
            tickets = Tickets.objects.create(show_id=show, Price=150)
            return Response({
                'id': tickets.id,
                'price': tickets.Price
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservedSeatDetailView(APIView):

    # renderer_classes = [JSONRenderer]

    def get(self, request, id):
        try:
            reserved_seat = Reserved_Seat.objects.get(id=id)
            serializer = ReservedSeatSerializer(reserved_seat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reserved_Seat.DoesNotExist:
            return Response({"Not Found": "Does Not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            reserved_seat = Reserved_Seat.objects.get(id=id)
            serializer = ReservedSeatSerializer(
                reserved_seat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reserved_Seat.DoesNotExist:
            return Response({"Not Found": "Does Not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            reserved_seat = Reserved_Seat.objects.get(id=id)
            reserved_seat.delete()
            return Response({"Deleted Successfully!!!"}, status=status.HTTP_404_NOT_FOUND)
        except Reserved_Seat.DoesNotExist:
            return Response({"Not Found": "Does Not exist"}, status=status.HTTP_404_NOT_FOUND)

# ////////        reserved seats     /////////


# ////////        ticket View       /////////
class TicketView(APIView):

    # renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            # user = User.objects.)
            tickets = Tickets.objects.all()
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tickets.DoesNotExist:
            return Response({"Not Found": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            send_reminder(topic="reminder-info", title="Booking Notification",
                          body="Your Show Will be held 1 hr before the booking evening")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, reserved_seat_id):
        try:
            reserved_seat = Reserved_Seat.objects.get(id=reserved_seat_id)
            ticket = Tickets.objects.get(seat_reserved_id=reserved_seat)
            serializer = TicketSerializer(ticket)
            return Response({
                "id": serializer.data['id'],
                "price": serializer.data['Price']
            }, status=status.HTTP_200_OK)
        except Tickets.DoesNotExist:
            return Response({"Not Found": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            ticket = Tickets.objects.get(id=id)
            serializer = TicketSerializer(ticket, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_100_CONTINUE)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tickets.DoesNotExist:
            return Response({"Not Found": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            ticket = Tickets.objects.get(id=id)
            ticket.delete()
            send_notification(
                user_id=ticket.user_id, title="Ticket Deleted Successfully", message="Deleted!", data=None)
            return Response({"Deleted Successfully!!!"}, status=status.HTTP_404_NOT_FOUND)
        except Tickets.DoesNotExist:
            return Response({"Not Found": "Does Not exist"}, status=status.HTTP_404_NOT_FOUND)


class TransectionView(APIView):

    def get(self, request):
        try:
            transections = Transection.objects.all()
            serializer = TransectionSerializer(transections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Transection.DoesNotExist:
            return Response({"Not Found": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args):
        serializer = TransectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesWatchedView(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            r_seats = Reserved_Seat.objects.filter(user_id=user)
            shows_list = []
            movies_list = []
            theater_list = []
            movie_history = []
            def getShows():
                for seat in r_seats.iterator():
                    show = Shows.objects.get(id=int(str(seat.show_id)))
                    shows_list.append(show)
            getShows()

            def getMovies():
                for i in range(len(shows_list)):
                    movie = Movies.objects.get(
                        id=int(str(shows_list[i].movie_id)))
                    movies_list.append(movie)
            getMovies()

            def getTheaters():
                for i in range(len(shows_list)):
                    theater = Theaters.objects.get(
                        id=int(str(shows_list[i].theater_id)))
                    theater_list.append(theater)
            getTheaters()

            for movie, theater, show in zip(movies_list, theater_list, shows_list):
                history = MoviesWatched.objects.create(
                    movie_name=movie.movie_name, cover_image=movie.cover_image, show_id=show.pk, show_time=show.show_time, date=show.date, theater_name=theater.theater_name)
                movie_history.append(history)
            movies = set(movie_history)

            serializer = MoviesWatchedSerializer(movies, many=True)
            return Response(
                serializer.data, status=status.HTTP_200_OK)
        except Reserved_Seat.DoesNotExist:
            pass


class Transections(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            r_seats = Reserved_Seat.objects.filter(user_id=user)

        except:
            pass

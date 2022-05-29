from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from movie.models import Movies
from .serializers import MovieSerializer
from accounts.models import User
from fcm_django.models import FCMDevice
from firebase_admin import messaging
from show.models import Transection

# Create your views here.

def send_notification():
    topic = 'cinema'
    message = messaging.Message(notification=messaging.Notification(
        title= "New Upcoming movie",
        body="Wrestle Mania"
    ))    
    response = FCMDevice.send_topic_message(message, topic)
    return response


class MovieView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        # get the list of all the movies
        try:
            movies = Movies.objects.filter(is_upcoming=False, is_recommended= False)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response("Model Does not exist")


class MovieDetailView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, id):
        # get the detail of a movie
        try:
            movie = Movies.objects.get(id=id)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response("Model Does Not exist")


class UpcomingMovieView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        # get the list of upcoming movies
        try:
            movie = Movies.objects.filter(is_upcoming=True)
            serializer = MovieSerializer(movie, many=True)
            send_notification()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Model Does not exist"}, status=status.HTTP_404_NOT_FOUND)

class RecommendedMovieView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id,is_premium_user=True)
            movies = Movies.objects.filter(user_id=user, is_recommended=True)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response("Movies Does not exist", status=status.HTTP_404_NOT_FOUND)

# class WatchedMovies(APIView):

#     def get(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             transaction = Transection.objects.filter(ticket)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from yaml import serialize
from movie.models import Movies
from .serializers import MovieSerializer

# Create your views here.


class MovieView(APIView):

    renderer_classes = [JSONRenderer]

    def get(self, request):
        # get the list of all the movies
        try:
            movies = Movies.objects.all()
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Model Does not exist")

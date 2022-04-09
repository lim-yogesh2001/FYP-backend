from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Theaters
from .serializer import MovieSerializer

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def theater_view(request):
    try:
        theaters = Theaters.objects.all()
        serializer = MovieSerializer(theaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Theaters.DoesNotExist:
        return Response("Theater Model Does not exist")


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def theater_details_view(request, id):
    try:
        theaters = Theaters.objects.get(id=id)
        serializer = MovieSerializer(theaters, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Theaters.DoesNotExist:
        return Response("Theater Model Does not exist")


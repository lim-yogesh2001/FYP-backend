from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import TheaterReviews, Theaters
from .serializer import TheaterReviewSerializer, TheaterSerializer, TheaterWriteReviewSerializer

# Create your views here.


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def theater_view(request):
    try:
        theaters = Theaters.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Theaters.DoesNotExist:
        return Response("Theater Model Does not exist", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def theater_details_view(request, id):
    try:
        theaters = Theaters.objects.get(id=id)
        serializer = TheaterSerializer(theaters, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Theaters.DoesNotExist:
        return Response("No Data of Theaters were found", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
# @renderer_classes([JSONRenderer])
def theater_reviews_view(request, theater_id):
    try:
        if request.method == 'GET':
            theater = Theaters.objects.get(id=theater_id)
            reviews = TheaterReviews.objects.filter(theater_id=theater)
            serializer = TheaterReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = TheaterWriteReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except TheaterReviews.DoesNotExist:
        return Response("No Data of Theater Reviews were found", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
# @renderer_classes([JSONRenderer])
def theater_reviews_detailviews(request, id):
    if request.method == 'GET':
        review = TheaterReviews.objects.get(id=id)
        serializer = TheaterReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        review = TheaterReviews.objects.get(id=id)
        serializer = TheaterReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review = TheaterReviews.objects.get(id=id)
        review.delete()
        return Response({"Deleted Successfully!!"}, status=status.HTTP_204_NO_CONTENT)
        

from django.urls import path
from .views import MovieView, UpcomingMovieView, MovieDetailView

urlpatterns = [
    path("movies/", MovieView.as_view(), name='movie-list'),
    path("movies/<int:id>/", MovieDetailView.as_view(), name='movie-detail'),
    path("upcoming-movies/", UpcomingMovieView.as_view(), name='upcoming-movies')
]



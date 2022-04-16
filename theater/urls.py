from django.urls import path
from . import views

urlpatterns = [
    path('theaters/', views.theater_view, name='theaters'),
    path('theaters/<int:id>/', views.theater_details_view, name='theater-detail'),
    path('theaters/reviews/<int:theater_id>/', views.theater_reviews_view, name='theater-review'),
    path('theaters/reviews-detail/<int:id>/', views.theater_reviews_detailviews, name="theater-review-details")
]

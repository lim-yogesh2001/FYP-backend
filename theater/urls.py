from django.urls import path
from . import views

urlpatterns = [
    path('theaters/', views.theater_view, name='theaters'),
    path('theaters/<int:id>/', views.theater_details_view, name='theater-detail')
]

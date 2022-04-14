from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password')
]

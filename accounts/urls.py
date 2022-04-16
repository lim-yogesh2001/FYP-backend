from django import views
from django.urls import path, include
from . import views
from knox import views as knox_views

urlpatterns = [
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', include('django_rest_passwordreset.urls'), name='password_reset')
]

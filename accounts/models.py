from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    phone_reggex = RegexValidator(regex=r'^\??\d{9,10}$', message= 'Please Enter the number in 9999999999 format.')
    phone = models.CharField(max_length=10, blank=True, validators=[phone_reggex])
    full_name = models.CharField(max_length=100, blank=True)

    def __srt__(self):
        return f"User {self.username}"
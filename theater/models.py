from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from accounts.models import User

# Create your models here.
class Theaters(models.Model):
    phone_reggex = RegexValidator(regex=r'^\??\d{9,10}$', message= 'Please Enter the number in 9999999999 format.')

    theater_name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to = 'images')
    contact = models.CharField(max_length=10, validators=[phone_reggex])
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    total_seats = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Theaters"

    def __str__(self):
        return f"{self.id}"


class TheaterReviews(models.Model):
    ratings = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    theater_id = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Theater Reviews"

    


from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "About us"


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Privacy Policy"

class BookingPolicy(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Booking Policy"





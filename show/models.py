import uuid
from django.db import models
from theater.models import Theaters
from movie.models import Movies
from accounts.models import User



class Shows(models.Model):
    show_time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    langauge = models.CharField(blank=False, max_length=100)
    theater_id = models.ForeignKey(Theaters, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Shows"

    def __str__(self):
        return f"Show {self.id}"


class Seats(models.Model):
    row = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    theater_id = models.ForeignKey(Theaters, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Seats"

    def __str__(self):
        return f"Seat {self.id}"


class Reserved_Seat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    seat_id = models.ForeignKey(Seats, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Shows, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserved Seats {self.id}"


class Tickets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Shows, on_delete=models.CASCADE)
    seat_reserved_id = models.ForeignKey(
        Reserved_Seat, on_delete=models.CASCADE)
    Price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return f"ticket {self.id}"
    
    

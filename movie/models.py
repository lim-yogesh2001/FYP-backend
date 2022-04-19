from tabnanny import verbose
from django.db import models
from accounts.models import User

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=100, verbose_name="movie name", null=False, blank=True)
    cover_image = models.ImageField(verbose_name="cover image", upload_to="images")
    release_date = models.DateField(verbose_name="release date")
    genres = models.CharField(max_length=100)
    director = models.CharField(max_length=150, blank=False)
    producers = models.CharField(max_length=100, blank=True, null=False)
    casts = models.CharField(max_length=100, default="Not Defined")
    descripton = models.TextField()
    is_upcoming = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    user_id = models.ManyToManyField(User, blank=True, verbose_name='premium_user')

    class Meta:
        verbose_name_plural = "Movies"
    
    def __str__(self):
        return f"{self.movie_name} {self.release_date}"
    
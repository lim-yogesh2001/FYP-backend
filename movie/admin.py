from django.contrib import admin
from .models import Movies

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name','cover_image', 'release_date', 'genres', 'director', 'producers', 'is_upcoming', 'is_popular',)

# Register your models here.
admin.site.register(Movies, MovieAdmin)
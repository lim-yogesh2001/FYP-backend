from django.contrib import admin
from .models import Theaters

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'theater_name','logo', 'contact', 'country', 'city', 'street', 'total_seats',)

# Register your models here.
admin.site.register(Theaters, TheaterAdmin)
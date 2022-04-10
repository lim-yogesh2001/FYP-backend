from django.contrib import admin
from .models import TheaterReviews, Theaters


class TheaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'theater_name', 'logo', 'contact',
                    'country', 'city', 'street', 'total_seats',)


class TheaterReviewAdmin(admin.ModelAdmin):
    list_filter = ('ratings',)
    list_display = ('id', 'ratings', 'comment', 'theater_id', 'user_id')


# Register your models here.
admin.site.register(Theaters, TheaterAdmin)
admin.site.register(TheaterReviews, TheaterReviewAdmin)

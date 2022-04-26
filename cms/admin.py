from django.contrib import admin
from .models import AboutUs, PrivacyPolicy, BookingPolicy

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(PrivacyPolicy)
admin.site.register(BookingPolicy)

from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name','date_joined', 'phone',)
# Register your models here.
admin.site.register(get_user_model(), UserAdmin)
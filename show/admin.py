from django.contrib import admin
from .models import Shows, Seats, Reserved_Seat, Tickets, Transection

class ShowAdmin(admin.ModelAdmin):
    list_filter = ('langauge',)
    list_display = ('id', 'show_time','date', 'langauge', 'theater_id', 'movie_id',)

class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'row', 'number', 'theater_id',)

class ReservedSeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'seat_id', 'show_id', 'reserved',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_id', 'Price', 'created', 'modified',)

# Register your models here.
admin.site.register(Shows, ShowAdmin)
admin.site.register(Seats, SeatAdmin)
admin.site.register(Reserved_Seat, ReservedSeatAdmin)
admin.site.register(Tickets, TicketAdmin)
admin.site.register(Transection)
# admin.site.register(BookedTickets)
# admin.site.register(ReservedTicket)
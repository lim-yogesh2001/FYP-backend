from django.urls import path
from .views import ReservedSeatView, ShowsDetailView, ShowsView, SeatView, TheaterSeatView, TicketView

urlpatterns = [
    path("shows/<int:movie_id>/", ShowsView.as_view(), name='movie-show'),
    path("show-details/<int:id>/", ShowsDetailView.as_view(), name='show-details'),
    path("seats/", SeatView.as_view(), name="seats-list"),
    path("seats/<int:theater_id>", TheaterSeatView.as_view(), name='theater-seat-list'),
    path("reserved-seats/", ReservedSeatView.as_view(), name='reserved-seats'),
    path("tickets/", TicketView.as_view(), name = 'ticket-lists')
]

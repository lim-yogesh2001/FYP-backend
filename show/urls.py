from django.urls import path
from .views import ShowsDetailView, ShowsView, SeatView, TheaterSeatView, TicketDetailView, TicketView, ReservedSeatView, ReservedSeatDetailView, TransectionView, TransectionDetailView, MoviesWatched
# BookedTicketView, BookedTicketDetailView, ReservedTicketView, ReservedTicketDetailView

urlpatterns = [
    path("shows/<int:movie_id>/", ShowsView.as_view(), name='movie-show'),
    path("show-details/<int:id>/", ShowsDetailView.as_view(), name='show-details'),
    path("seats/", SeatView.as_view(), name="seats-list"),
    path("seats/<int:theater_id>", TheaterSeatView.as_view(),
         name='theater-seat-list'),
    path("reserved-seats/", ReservedSeatView.as_view(), name='reserved-seats'),
    path("reserved-seats/<int:id>", ReservedSeatDetailView.as_view(),
         name='reserved-seats-detail'),
    path("tickets/<int:user_id>", TicketView.as_view(), name='ticket-lists'),
    path("tickets/details/<int:reserved_seat_id>",
         TicketDetailView.as_view(), name='ticket-details'),
    path("transections/", TransectionView.as_view(), name='transection-list'),
    path("transections/<int:ticket_id>", TransectionDetailView.as_view(), name='transection-detail'),
    path("movies-watched/<int:user_id>",MoviesWatched.as_view(), name='movies-watched')
]

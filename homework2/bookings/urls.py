from django.urls import path
from . import views

# creates an URL for bookings
urlpatterns = [
    path('movies/', views.movie_list, name="Movies"),
    path('seats/', views.seats_list, name="Seat View"),
]
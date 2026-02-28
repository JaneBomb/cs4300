from django.shortcuts import render
from django.http import JsonResponse
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from .models import Movie, Seat, Booking
from rest_framework import viewsets

from rest_framework import permissions
from django.contrib.auth.models import User

# Create your views here.
#---------------------------- HTML VIEWS ----------------------------------#
def test_base(request):
    return render(request, 'bookings/base.html')

#---------------------------- APIS ----------------------------------#
class MovieViewSet(viewsets.ModelViewSet):
    '''
    Recieves all the movies objects. Calls the serializer.
    Displays the data in json format.
    '''

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class SeatViewSet(viewsets.ModelViewSet):
    '''
    Recieves all the seat objects. Calls the serializer.
    Displays the data in json format.
    '''
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingsViewSet(viewsets.ModelViewSet):
    '''
    Recieves all the booking objects for the user. Calls the serializer.
    Displays the data in json format.
    '''
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    '''
    # Ensures that the bookings for specific user are gotten
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user) 
    '''

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

'''
class UserBookingListAPIView(generics.ListAPIView):
    
    Will only show all the bookings for the specific user
    Includes past bookings
    

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Ensures that the bookings for specific user are gotten
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
'''
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import MovieSerializer
from .models import Movie

from rest_framework.response import response
from rest_framework import viewsets

# Create your views here.
#class MovieViewSet(viewsets.ModelViewSet):
'''
def movie_list(request):
    
    Recieves all the movies objects. Calls the serializer.
    Displays the data in json format.
    
    queryset = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse({
        'data': serializer.data
    })
'''


def seat_list(request):
    seats = Seat.objects.all()
    serializer = SeatSerializer(seats, many=True)
    return JsonResponse({ 
        'data': serializer.data
    })